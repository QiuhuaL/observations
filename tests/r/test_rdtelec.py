from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rdtelec import rdtelec


def test_rdtelec():
  """Test module rdtelec.py by downloading
   rdtelec.csv and testing shape of
   extracted data has 29 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rdtelec(test_path)
  try:
    assert x_train.shape == (29, 6)
  except:
    shutil.rmtree(test_path)
    raise()
