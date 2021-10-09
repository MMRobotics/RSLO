# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rslo/protos/losses.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rslo/protos/losses.proto',
  package='second.protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18rslo/protos/losses.proto\x12\rsecond.protos\"\x86\x03\n\x04Loss\x12\x31\n\rrotation_loss\x18\x01 \x01(\x0b\x32\x1a.second.protos.RotaionLoss\x12\x38\n\x10translation_loss\x18\x02 \x01(\x0b\x32\x1e.second.protos.TranslationLoss\x12\x39\n\x15pyramid_rotation_loss\x18\x03 \x01(\x0b\x32\x1a.second.protos.RotaionLoss\x12@\n\x18pyramid_translation_loss\x18\x04 \x01(\x0b\x32\x1e.second.protos.TranslationLoss\x12\x38\n\x10\x63onsistency_loss\x18\x05 \x01(\x0b\x32\x1e.second.protos.ConsistencyLoss\x12\x19\n\x11pyloss_exp_w_base\x18\x06 \x01(\x02\x12?\n\x14rigid_transform_loss\x18\x07 \x01(\x0b\x32!.second.protos.RigidTransformLoss\"9\n\x12RigidTransformLoss\x12\x0e\n\x06weight\x18\x02 \x01(\x02\x12\x13\n\x0b\x66ocal_gamma\x18\x05 \x01(\x02\"\x89\x01\n\x0bRotaionLoss\x12\x11\n\tloss_type\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\x02\x12\x12\n\ninit_alpha\x18\x03 \x01(\x02\x12\x17\n\x0fnot_learn_alpha\x18\x04 \x01(\x08\x12\x13\n\x0b\x66ocal_gamma\x18\x05 \x01(\x02\x12\x15\n\rbalance_scale\x18\x06 \x01(\x02\"\x8d\x01\n\x0fTranslationLoss\x12\x11\n\tloss_type\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\x02\x12\x12\n\ninit_alpha\x18\x03 \x01(\x02\x12\x17\n\x0fnot_learn_alpha\x18\x04 \x01(\x08\x12\x13\n\x0b\x66ocal_gamma\x18\x05 \x01(\x02\x12\x15\n\rbalance_scale\x18\x06 \x01(\x02\"\xfe\x01\n\x0f\x43onsistencyLoss\x12\x11\n\tloss_type\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\x02\x12\x12\n\ninit_alpha\x18\x03 \x01(\x02\x12\x17\n\x0fnot_learn_alpha\x18\x04 \x01(\x08\x12\x13\n\x0b\x66ocal_gamma\x18\x05 \x01(\x02\x12\x16\n\x0epenalize_ratio\x18\x06 \x01(\x02\x12\x19\n\x11sample_block_size\x18\x07 \x03(\x02\x12\x0c\n\x04norm\x18\x08 \x01(\x08\x12\x1d\n\x15pred_downsample_ratio\x18\t \x01(\x02\x12\x12\n\nreg_weight\x18\n \x01(\x02\x12\x12\n\nsph_weight\x18\x0b \x01(\x02\x62\x06proto3')
)




_LOSS = _descriptor.Descriptor(
  name='Loss',
  full_name='second.protos.Loss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotation_loss', full_name='second.protos.Loss.rotation_loss', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translation_loss', full_name='second.protos.Loss.translation_loss', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pyramid_rotation_loss', full_name='second.protos.Loss.pyramid_rotation_loss', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pyramid_translation_loss', full_name='second.protos.Loss.pyramid_translation_loss', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consistency_loss', full_name='second.protos.Loss.consistency_loss', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pyloss_exp_w_base', full_name='second.protos.Loss.pyloss_exp_w_base', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rigid_transform_loss', full_name='second.protos.Loss.rigid_transform_loss', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=434,
)


_RIGIDTRANSFORMLOSS = _descriptor.Descriptor(
  name='RigidTransformLoss',
  full_name='second.protos.RigidTransformLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='second.protos.RigidTransformLoss.weight', index=0,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focal_gamma', full_name='second.protos.RigidTransformLoss.focal_gamma', index=1,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=493,
)


_ROTAIONLOSS = _descriptor.Descriptor(
  name='RotaionLoss',
  full_name='second.protos.RotaionLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loss_type', full_name='second.protos.RotaionLoss.loss_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='second.protos.RotaionLoss.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_alpha', full_name='second.protos.RotaionLoss.init_alpha', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_learn_alpha', full_name='second.protos.RotaionLoss.not_learn_alpha', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focal_gamma', full_name='second.protos.RotaionLoss.focal_gamma', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance_scale', full_name='second.protos.RotaionLoss.balance_scale', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=496,
  serialized_end=633,
)


_TRANSLATIONLOSS = _descriptor.Descriptor(
  name='TranslationLoss',
  full_name='second.protos.TranslationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loss_type', full_name='second.protos.TranslationLoss.loss_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='second.protos.TranslationLoss.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_alpha', full_name='second.protos.TranslationLoss.init_alpha', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_learn_alpha', full_name='second.protos.TranslationLoss.not_learn_alpha', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focal_gamma', full_name='second.protos.TranslationLoss.focal_gamma', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance_scale', full_name='second.protos.TranslationLoss.balance_scale', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=777,
)


_CONSISTENCYLOSS = _descriptor.Descriptor(
  name='ConsistencyLoss',
  full_name='second.protos.ConsistencyLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loss_type', full_name='second.protos.ConsistencyLoss.loss_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='second.protos.ConsistencyLoss.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_alpha', full_name='second.protos.ConsistencyLoss.init_alpha', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_learn_alpha', full_name='second.protos.ConsistencyLoss.not_learn_alpha', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focal_gamma', full_name='second.protos.ConsistencyLoss.focal_gamma', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='penalize_ratio', full_name='second.protos.ConsistencyLoss.penalize_ratio', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_block_size', full_name='second.protos.ConsistencyLoss.sample_block_size', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='norm', full_name='second.protos.ConsistencyLoss.norm', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pred_downsample_ratio', full_name='second.protos.ConsistencyLoss.pred_downsample_ratio', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reg_weight', full_name='second.protos.ConsistencyLoss.reg_weight', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sph_weight', full_name='second.protos.ConsistencyLoss.sph_weight', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=780,
  serialized_end=1034,
)

_LOSS.fields_by_name['rotation_loss'].message_type = _ROTAIONLOSS
_LOSS.fields_by_name['translation_loss'].message_type = _TRANSLATIONLOSS
_LOSS.fields_by_name['pyramid_rotation_loss'].message_type = _ROTAIONLOSS
_LOSS.fields_by_name['pyramid_translation_loss'].message_type = _TRANSLATIONLOSS
_LOSS.fields_by_name['consistency_loss'].message_type = _CONSISTENCYLOSS
_LOSS.fields_by_name['rigid_transform_loss'].message_type = _RIGIDTRANSFORMLOSS
DESCRIPTOR.message_types_by_name['Loss'] = _LOSS
DESCRIPTOR.message_types_by_name['RigidTransformLoss'] = _RIGIDTRANSFORMLOSS
DESCRIPTOR.message_types_by_name['RotaionLoss'] = _ROTAIONLOSS
DESCRIPTOR.message_types_by_name['TranslationLoss'] = _TRANSLATIONLOSS
DESCRIPTOR.message_types_by_name['ConsistencyLoss'] = _CONSISTENCYLOSS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Loss = _reflection.GeneratedProtocolMessageType('Loss', (_message.Message,), {
  'DESCRIPTOR' : _LOSS,
  '__module__' : 'rslo.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.Loss)
  })
_sym_db.RegisterMessage(Loss)

RigidTransformLoss = _reflection.GeneratedProtocolMessageType('RigidTransformLoss', (_message.Message,), {
  'DESCRIPTOR' : _RIGIDTRANSFORMLOSS,
  '__module__' : 'rslo.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.RigidTransformLoss)
  })
_sym_db.RegisterMessage(RigidTransformLoss)

RotaionLoss = _reflection.GeneratedProtocolMessageType('RotaionLoss', (_message.Message,), {
  'DESCRIPTOR' : _ROTAIONLOSS,
  '__module__' : 'rslo.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.RotaionLoss)
  })
_sym_db.RegisterMessage(RotaionLoss)

TranslationLoss = _reflection.GeneratedProtocolMessageType('TranslationLoss', (_message.Message,), {
  'DESCRIPTOR' : _TRANSLATIONLOSS,
  '__module__' : 'rslo.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.TranslationLoss)
  })
_sym_db.RegisterMessage(TranslationLoss)

ConsistencyLoss = _reflection.GeneratedProtocolMessageType('ConsistencyLoss', (_message.Message,), {
  'DESCRIPTOR' : _CONSISTENCYLOSS,
  '__module__' : 'rslo.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.ConsistencyLoss)
  })
_sym_db.RegisterMessage(ConsistencyLoss)


# @@protoc_insertion_point(module_scope)