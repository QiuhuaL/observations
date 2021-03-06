from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.river_elements import river_elements


def test_river_elements():
  """Test module river_elements.py by downloading
   river_elements.csv and testing shape of
   extracted data has 12 rows and 27 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = river_elements(test_path)
  try:
    assert x_train.shape == (12, 27)
  except:
    shutil.rmtree(test_path)
    raise()
