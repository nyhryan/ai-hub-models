# ---------------------------------------------------------------------
# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from qai_hub_models.models._shared.whisper.demo import whisper_demo
from qai_hub_models.models.whisper_tiny_multi.model import WhisperTinyMulti


def main(is_test: bool = False):
    whisper_demo(WhisperTinyMulti, is_test)


if __name__ == "__main__":
    main()
