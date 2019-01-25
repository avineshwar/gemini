# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.gogo.protobuf.gogoproto import gogo_pb2 as github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2
import importlib
gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2 = importlib.import_module('gopkg.in.bblfsh.sdk.v1.uast.generated_pb2')


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='tech.sourced.featurext.generated',
  syntax='proto3',
  serialized_pb=_b('\n\rservice.proto\x12 tech.sourced.featurext.generated\x1a-github.com/gogo/protobuf/gogoproto/gogo.proto\x1a+gopkg.in/bblfsh/sdk.v1/uast/generated.proto\"Q\n\x12IdentifiersOptions\x12\x18\n\x10\x64ocfreqThreshold\x18\x01 \x01(\x05\x12\x0e\n\x06weight\x18\x02 \x01(\x05\x12\x11\n\tsplitStem\x18\x03 \x01(\x08\";\n\x0fLiteralsOptions\x12\x18\n\x10\x64ocfreqThreshold\x18\x01 \x01(\x05\x12\x0e\n\x06weight\x18\x02 \x01(\x05\"[\n\x0fUast2seqOptions\x12\x18\n\x10\x64ocfreqThreshold\x18\x01 \x01(\x05\x12\x0e\n\x06weight\x18\x02 \x01(\x05\x12\x0e\n\x06stride\x18\x03 \x01(\x05\x12\x0e\n\x06seqLen\x18\x04 \x03(\x05\";\n\x0fGraphletOptions\x12\x18\n\x10\x64ocfreqThreshold\x18\x01 \x01(\x05\x12\x0e\n\x06weight\x18\x02 \x01(\x05\"\xdb\x02\n\x0e\x45xtractRequest\x12/\n\x04uast\x18\x01 \x01(\x0b\x32!.gopkg.in.bblfsh.sdk.v1.uast.Node\x12I\n\x0bidentifiers\x18\x02 \x01(\x0b\x32\x34.tech.sourced.featurext.generated.IdentifiersOptions\x12\x43\n\x08literals\x18\x03 \x01(\x0b\x32\x31.tech.sourced.featurext.generated.LiteralsOptions\x12\x43\n\x08uast2seq\x18\x04 \x01(\x0b\x32\x31.tech.sourced.featurext.generated.Uast2seqOptions\x12\x43\n\x08graphlet\x18\x05 \x01(\x0b\x32\x31.tech.sourced.featurext.generated.GraphletOptions\"\x8c\x01\n\x12IdentifiersRequest\x12/\n\x04uast\x18\x01 \x01(\x0b\x32!.gopkg.in.bblfsh.sdk.v1.uast.Node\x12\x45\n\x07options\x18\x02 \x01(\x0b\x32\x34.tech.sourced.featurext.generated.IdentifiersOptions\"\x86\x01\n\x0fLiteralsRequest\x12/\n\x04uast\x18\x01 \x01(\x0b\x32!.gopkg.in.bblfsh.sdk.v1.uast.Node\x12\x42\n\x07options\x18\x02 \x01(\x0b\x32\x31.tech.sourced.featurext.generated.LiteralsOptions\"\x86\x01\n\x0fUast2seqRequest\x12/\n\x04uast\x18\x01 \x01(\x0b\x32!.gopkg.in.bblfsh.sdk.v1.uast.Node\x12\x42\n\x07options\x18\x02 \x01(\x0b\x32\x31.tech.sourced.featurext.generated.Uast2seqOptions\"\x86\x01\n\x0fGraphletRequest\x12/\n\x04uast\x18\x01 \x01(\x0b\x32!.gopkg.in.bblfsh.sdk.v1.uast.Node\x12\x42\n\x07options\x18\x02 \x01(\x0b\x32\x31.tech.sourced.featurext.generated.GraphletOptions\"\'\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\x02\"L\n\rFeaturesReply\x12;\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32).tech.sourced.featurext.generated.Feature2\xd0\x04\n\x10\x46\x65\x61tureExtractor\x12n\n\x07\x45xtract\x12\x30.tech.sourced.featurext.generated.ExtractRequest\x1a/.tech.sourced.featurext.generated.FeaturesReply\"\x00\x12v\n\x0bIdentifiers\x12\x34.tech.sourced.featurext.generated.IdentifiersRequest\x1a/.tech.sourced.featurext.generated.FeaturesReply\"\x00\x12p\n\x08Literals\x12\x31.tech.sourced.featurext.generated.LiteralsRequest\x1a/.tech.sourced.featurext.generated.FeaturesReply\"\x00\x12p\n\x08Uast2seq\x12\x31.tech.sourced.featurext.generated.Uast2seqRequest\x1a/.tech.sourced.featurext.generated.FeaturesReply\"\x00\x12p\n\x08Graphlet\x12\x31.tech.sourced.featurext.generated.GraphletRequest\x1a/.tech.sourced.featurext.generated.FeaturesReply\"\x00\x62\x06proto3')
  ,
  dependencies=[github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2.DESCRIPTOR,])




_IDENTIFIERSOPTIONS = _descriptor.Descriptor(
  name='IdentifiersOptions',
  full_name='tech.sourced.featurext.generated.IdentifiersOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docfreqThreshold', full_name='tech.sourced.featurext.generated.IdentifiersOptions.docfreqThreshold', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tech.sourced.featurext.generated.IdentifiersOptions.weight', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='splitStem', full_name='tech.sourced.featurext.generated.IdentifiersOptions.splitStem', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=224,
)


_LITERALSOPTIONS = _descriptor.Descriptor(
  name='LiteralsOptions',
  full_name='tech.sourced.featurext.generated.LiteralsOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docfreqThreshold', full_name='tech.sourced.featurext.generated.LiteralsOptions.docfreqThreshold', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tech.sourced.featurext.generated.LiteralsOptions.weight', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=285,
)


_UAST2SEQOPTIONS = _descriptor.Descriptor(
  name='Uast2seqOptions',
  full_name='tech.sourced.featurext.generated.Uast2seqOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docfreqThreshold', full_name='tech.sourced.featurext.generated.Uast2seqOptions.docfreqThreshold', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tech.sourced.featurext.generated.Uast2seqOptions.weight', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stride', full_name='tech.sourced.featurext.generated.Uast2seqOptions.stride', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqLen', full_name='tech.sourced.featurext.generated.Uast2seqOptions.seqLen', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=378,
)


_GRAPHLETOPTIONS = _descriptor.Descriptor(
  name='GraphletOptions',
  full_name='tech.sourced.featurext.generated.GraphletOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docfreqThreshold', full_name='tech.sourced.featurext.generated.GraphletOptions.docfreqThreshold', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tech.sourced.featurext.generated.GraphletOptions.weight', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=439,
)


_EXTRACTREQUEST = _descriptor.Descriptor(
  name='ExtractRequest',
  full_name='tech.sourced.featurext.generated.ExtractRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uast', full_name='tech.sourced.featurext.generated.ExtractRequest.uast', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='tech.sourced.featurext.generated.ExtractRequest.identifiers', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='literals', full_name='tech.sourced.featurext.generated.ExtractRequest.literals', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uast2seq', full_name='tech.sourced.featurext.generated.ExtractRequest.uast2seq', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graphlet', full_name='tech.sourced.featurext.generated.ExtractRequest.graphlet', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=789,
)


_IDENTIFIERSREQUEST = _descriptor.Descriptor(
  name='IdentifiersRequest',
  full_name='tech.sourced.featurext.generated.IdentifiersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uast', full_name='tech.sourced.featurext.generated.IdentifiersRequest.uast', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='tech.sourced.featurext.generated.IdentifiersRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=792,
  serialized_end=932,
)


_LITERALSREQUEST = _descriptor.Descriptor(
  name='LiteralsRequest',
  full_name='tech.sourced.featurext.generated.LiteralsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uast', full_name='tech.sourced.featurext.generated.LiteralsRequest.uast', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='tech.sourced.featurext.generated.LiteralsRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=935,
  serialized_end=1069,
)


_UAST2SEQREQUEST = _descriptor.Descriptor(
  name='Uast2seqRequest',
  full_name='tech.sourced.featurext.generated.Uast2seqRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uast', full_name='tech.sourced.featurext.generated.Uast2seqRequest.uast', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='tech.sourced.featurext.generated.Uast2seqRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1072,
  serialized_end=1206,
)


_GRAPHLETREQUEST = _descriptor.Descriptor(
  name='GraphletRequest',
  full_name='tech.sourced.featurext.generated.GraphletRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uast', full_name='tech.sourced.featurext.generated.GraphletRequest.uast', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='tech.sourced.featurext.generated.GraphletRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1209,
  serialized_end=1343,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='tech.sourced.featurext.generated.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tech.sourced.featurext.generated.Feature.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tech.sourced.featurext.generated.Feature.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1345,
  serialized_end=1384,
)


_FEATURESREPLY = _descriptor.Descriptor(
  name='FeaturesReply',
  full_name='tech.sourced.featurext.generated.FeaturesReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='tech.sourced.featurext.generated.FeaturesReply.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1386,
  serialized_end=1462,
)

_EXTRACTREQUEST.fields_by_name['uast'].message_type = gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2._NODE
_EXTRACTREQUEST.fields_by_name['identifiers'].message_type = _IDENTIFIERSOPTIONS
_EXTRACTREQUEST.fields_by_name['literals'].message_type = _LITERALSOPTIONS
_EXTRACTREQUEST.fields_by_name['uast2seq'].message_type = _UAST2SEQOPTIONS
_EXTRACTREQUEST.fields_by_name['graphlet'].message_type = _GRAPHLETOPTIONS
_IDENTIFIERSREQUEST.fields_by_name['uast'].message_type = gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2._NODE
_IDENTIFIERSREQUEST.fields_by_name['options'].message_type = _IDENTIFIERSOPTIONS
_LITERALSREQUEST.fields_by_name['uast'].message_type = gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2._NODE
_LITERALSREQUEST.fields_by_name['options'].message_type = _LITERALSOPTIONS
_UAST2SEQREQUEST.fields_by_name['uast'].message_type = gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2._NODE
_UAST2SEQREQUEST.fields_by_name['options'].message_type = _UAST2SEQOPTIONS
_GRAPHLETREQUEST.fields_by_name['uast'].message_type = gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2._NODE
_GRAPHLETREQUEST.fields_by_name['options'].message_type = _GRAPHLETOPTIONS
_FEATURESREPLY.fields_by_name['features'].message_type = _FEATURE
DESCRIPTOR.message_types_by_name['IdentifiersOptions'] = _IDENTIFIERSOPTIONS
DESCRIPTOR.message_types_by_name['LiteralsOptions'] = _LITERALSOPTIONS
DESCRIPTOR.message_types_by_name['Uast2seqOptions'] = _UAST2SEQOPTIONS
DESCRIPTOR.message_types_by_name['GraphletOptions'] = _GRAPHLETOPTIONS
DESCRIPTOR.message_types_by_name['ExtractRequest'] = _EXTRACTREQUEST
DESCRIPTOR.message_types_by_name['IdentifiersRequest'] = _IDENTIFIERSREQUEST
DESCRIPTOR.message_types_by_name['LiteralsRequest'] = _LITERALSREQUEST
DESCRIPTOR.message_types_by_name['Uast2seqRequest'] = _UAST2SEQREQUEST
DESCRIPTOR.message_types_by_name['GraphletRequest'] = _GRAPHLETREQUEST
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['FeaturesReply'] = _FEATURESREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IdentifiersOptions = _reflection.GeneratedProtocolMessageType('IdentifiersOptions', (_message.Message,), dict(
  DESCRIPTOR = _IDENTIFIERSOPTIONS,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.IdentifiersOptions)
  ))
_sym_db.RegisterMessage(IdentifiersOptions)

LiteralsOptions = _reflection.GeneratedProtocolMessageType('LiteralsOptions', (_message.Message,), dict(
  DESCRIPTOR = _LITERALSOPTIONS,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.LiteralsOptions)
  ))
_sym_db.RegisterMessage(LiteralsOptions)

Uast2seqOptions = _reflection.GeneratedProtocolMessageType('Uast2seqOptions', (_message.Message,), dict(
  DESCRIPTOR = _UAST2SEQOPTIONS,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.Uast2seqOptions)
  ))
_sym_db.RegisterMessage(Uast2seqOptions)

GraphletOptions = _reflection.GeneratedProtocolMessageType('GraphletOptions', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHLETOPTIONS,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.GraphletOptions)
  ))
_sym_db.RegisterMessage(GraphletOptions)

ExtractRequest = _reflection.GeneratedProtocolMessageType('ExtractRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXTRACTREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.ExtractRequest)
  ))
_sym_db.RegisterMessage(ExtractRequest)

IdentifiersRequest = _reflection.GeneratedProtocolMessageType('IdentifiersRequest', (_message.Message,), dict(
  DESCRIPTOR = _IDENTIFIERSREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.IdentifiersRequest)
  ))
_sym_db.RegisterMessage(IdentifiersRequest)

LiteralsRequest = _reflection.GeneratedProtocolMessageType('LiteralsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LITERALSREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.LiteralsRequest)
  ))
_sym_db.RegisterMessage(LiteralsRequest)

Uast2seqRequest = _reflection.GeneratedProtocolMessageType('Uast2seqRequest', (_message.Message,), dict(
  DESCRIPTOR = _UAST2SEQREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.Uast2seqRequest)
  ))
_sym_db.RegisterMessage(Uast2seqRequest)

GraphletRequest = _reflection.GeneratedProtocolMessageType('GraphletRequest', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHLETREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.GraphletRequest)
  ))
_sym_db.RegisterMessage(GraphletRequest)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.Feature)
  ))
_sym_db.RegisterMessage(Feature)

FeaturesReply = _reflection.GeneratedProtocolMessageType('FeaturesReply', (_message.Message,), dict(
  DESCRIPTOR = _FEATURESREPLY,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:tech.sourced.featurext.generated.FeaturesReply)
  ))
_sym_db.RegisterMessage(FeaturesReply)



_FEATUREEXTRACTOR = _descriptor.ServiceDescriptor(
  name='FeatureExtractor',
  full_name='tech.sourced.featurext.generated.FeatureExtractor',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1465,
  serialized_end=2057,
  methods=[
  _descriptor.MethodDescriptor(
    name='Extract',
    full_name='tech.sourced.featurext.generated.FeatureExtractor.Extract',
    index=0,
    containing_service=None,
    input_type=_EXTRACTREQUEST,
    output_type=_FEATURESREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Identifiers',
    full_name='tech.sourced.featurext.generated.FeatureExtractor.Identifiers',
    index=1,
    containing_service=None,
    input_type=_IDENTIFIERSREQUEST,
    output_type=_FEATURESREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Literals',
    full_name='tech.sourced.featurext.generated.FeatureExtractor.Literals',
    index=2,
    containing_service=None,
    input_type=_LITERALSREQUEST,
    output_type=_FEATURESREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Uast2seq',
    full_name='tech.sourced.featurext.generated.FeatureExtractor.Uast2seq',
    index=3,
    containing_service=None,
    input_type=_UAST2SEQREQUEST,
    output_type=_FEATURESREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Graphlet',
    full_name='tech.sourced.featurext.generated.FeatureExtractor.Graphlet',
    index=4,
    containing_service=None,
    input_type=_GRAPHLETREQUEST,
    output_type=_FEATURESREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FEATUREEXTRACTOR)

DESCRIPTOR.services_by_name['FeatureExtractor'] = _FEATUREEXTRACTOR

# @@protoc_insertion_point(module_scope)
