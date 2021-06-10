#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "7edb707a-eaf5-4a2b-ae9a-440bc2aa9f10")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "wj6f?f%+kB.%(Qj71jUIE{yP>54w>oD")
