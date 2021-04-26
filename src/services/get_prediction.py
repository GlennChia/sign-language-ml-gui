import sys
import os
import re
import numpy as np
import torch
from torchvision import transforms
# services
from services.get_test_labels import get_test_video_name_to_class_id
from services.get_class_id_labels import get_class_id_to_label
# paths to models and utils
module_path = os.path.abspath(os.path.join("../"))
if module_path not in sys.path:
  sys.path.append(module_path)
from models.models import CNN_RNN
from utils.extract_frames import extract_frames

def format_list_to_torch(frames):
  """Convert list of numpy.array to numpy.array of format (batch_size, timesteps, C, H, W)

  Parameters:
  frames (list of numpy.array): list of frames

  Returns:
  numpy.array: vid_arr

  """
  formatted_frames = np.array(frames)
  formatted_frames = torch.from_numpy(formatted_frames).float()
  formatted_frames = formatted_frames.unsqueeze(0)
  formatted_frames = formatted_frames.unsqueeze(2)
  return formatted_frames

def get_prediction(video_name, video_path, model_path, test_label_path, label_meta_path):
  """Get predictions and ground truth (if video is in the test dataset) from the input video

  Parameters:
  video_name (str): video name without .mp4 extension
  video_path (str): path to video
  model_path (str): path to trained model
  test_label_path (str): path to csv that has class ids for test videos 
  label_meta_path (str): path to csv that has label values for class ids

  Returns:
  str: ground_truth
  str: output_label

  """
  test_video_name_to_class_id = get_test_video_name_to_class_id(test_label_path)
  class_id_to_label, num_classes = get_class_id_to_label(label_meta_path)
  transforms_compose = transforms.Compose([transforms.Resize(256), 
                                         transforms.CenterCrop(200),
                                         transforms.Grayscale()])
  frames = extract_frames(video_path, 30, transforms=transforms_compose)
  formatted_frames = format_list_to_torch(frames)
  
  model = CNN_RNN(num_classes, 30, 1, 1, channel_in=1, device="cpu")
  model_state_dict = torch.load(model_path, map_location=torch.device("cpu"))
  model.load_state_dict(model_state_dict)

  output = model.forward(formatted_frames)
  output = output.argmax(1)
  output = output.item()

  output_label = class_id_to_label[output]
  try:
    video_name = re.search("signer\d+_sample\d+", video_name).group()
    ground_truth = test_video_name_to_class_id[video_name]
    ground_truth = class_id_to_label[ground_truth]
  except:
    ground_truth = ""
  return ground_truth, output_label