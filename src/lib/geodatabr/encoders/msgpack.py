#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Paulo Freitas
# MIT License (see LICENSE file)
"""MessagePack encoder module."""
# Imports

# External dependencies

import msgpack

# Package dependencies

from geodatabr.core import encoders
from geodatabr.core.utils import io
from geodatabr.dataset import serializers

# Classes


class MessagePackFormat(encoders.EncoderFormat):
    """Encoder format class for MessagePack file format."""

    @property
    def name(self) -> str:
        """Gets the encoder format name."""
        return 'msgpack'

    @property
    def friendlyName(self) -> str:
        """Gets the encoder format friendly name."""
        return 'MessagePack'

    @property
    def extension(self) -> str:
        """Gets the encoder format extension."""
        return '.msgpack'

    @property
    def type(self) -> str:
        """Gets the encoder format type."""
        return 'Data Interchange'

    @property
    def mimeType(self) -> str:
        """Gets the encoder format media type."""
        return 'application/x-msgpack'

    @property
    def info(self) -> str:
        """Gets the encoder format reference info."""
        return 'https://en.wikipedia.org/wiki/MessagePack'

    @property
    def isBinary(self) -> bool:
        """Tells whether the encoder format is binary or not."""
        return True


class MessagePackEncoder(encoders.Encoder):
    """
    MessagePack encoder class.

    Attributes:
        format (geodatabr.encoders.msgpack.MessagePackFormat):
            The encoder format class
        serializer (geodatabr.dataset.serializers):
            The encoder serialization class
    """

    format = MessagePackFormat
    serializer = serializers.Serializer

    @property
    def options(self) -> dict:
        """Gets the default encoding options."""
        return dict(use_bin_type=False)

    def encode(self, data: dict, **options) -> io.BinaryFileStream:
        """
        Encodes the data into a MessagePack file-like stream.

        Args:
            data: The data to encode
            **options: The encoding options

        Returns:
            A MessagePack file-like stream

        Raises:
            geodatabr.core.encoders.EncodeError: If data fails to encode
        """
        try:
            return io.BinaryFileStream(
                msgpack.packb(data, **dict(self.options, **options)))
        except Exception:
            raise encoders.EncodeError
