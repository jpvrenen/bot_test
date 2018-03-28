#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import argparse
import yaml
import logging
import logging.config

#logging section
logger = logging.getLogger(__name__)
log_config_file = "D:/DATA/Company/Werkmap/Scripting/Python/bot_test/log/logging.yaml"
with open(log_config_file, 'r') as f:
    log_config = yaml.safe_load(f.read())
logging.config.dictConfig(log_config)

logger.info("blabla")