# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mesh.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Mesh.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nMesh.proto\"9\n\x0b\x46loat4Proto\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"x\n\x0eTransformProto\x12\x18\n\x02\x63\x31\x18\x01 \x01(\x0b\x32\x0c.Float4Proto\x12\x18\n\x02\x63\x32\x18\x02 \x01(\x0b\x32\x0c.Float4Proto\x12\x18\n\x02\x63\x33\x18\x03 \x01(\x0b\x32\x0c.Float4Proto\x12\x18\n\x02\x63\x34\x18\x04 \x01(\x0b\x32\x0c.Float4Proto\"O\n\x0bVertexProto\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01u\x18\x04 \x01(\x02\x12\t\n\x01v\x18\x05 \x01(\x02\x12\t\n\x01w\x18\x06 \x01(\x02\"[\n\tMeshProto\x12\x1e\n\x08vertices\x18\x01 \x03(\x0b\x32\x0c.VertexProto\x12\"\n\ttransform\x18\x02 \x01(\x0b\x32\x0f.TransformProto\x12\n\n\x02id\x18\x03 \x01(\t\")\n\x0bMeshesProto\x12\x1a\n\x06meshes\x18\x01 \x03(\x0b\x32\n.MeshProto\"?\n\x11\x44irectionAndDepth\x12\t\n\x01u\x18\x01 \x01(\x02\x12\t\n\x01v\x18\x02 \x01(\x02\x12\t\n\x01w\x18\x03 \x01(\x02\x12\t\n\x01\x64\x18\x04 \x01(\x02\",\n\x06Points\x12\"\n\x06points\x18\x01 \x03(\x0b\x32\x12.DirectionAndDepthb\x06proto3'
)




_FLOAT4PROTO = _descriptor.Descriptor(
  name='Float4Proto',
  full_name='Float4Proto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Float4Proto.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='Float4Proto.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='Float4Proto.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='Float4Proto.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=14,
  serialized_end=71,
)


_TRANSFORMPROTO = _descriptor.Descriptor(
  name='TransformProto',
  full_name='TransformProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c1', full_name='TransformProto.c1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c2', full_name='TransformProto.c2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c3', full_name='TransformProto.c3', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c4', full_name='TransformProto.c4', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=73,
  serialized_end=193,
)


_VERTEXPROTO = _descriptor.Descriptor(
  name='VertexProto',
  full_name='VertexProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='VertexProto.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='VertexProto.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='VertexProto.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='u', full_name='VertexProto.u', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v', full_name='VertexProto.v', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='VertexProto.w', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=195,
  serialized_end=274,
)


_MESHPROTO = _descriptor.Descriptor(
  name='MeshProto',
  full_name='MeshProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertices', full_name='MeshProto.vertices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transform', full_name='MeshProto.transform', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='MeshProto.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=276,
  serialized_end=367,
)


_MESHESPROTO = _descriptor.Descriptor(
  name='MeshesProto',
  full_name='MeshesProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meshes', full_name='MeshesProto.meshes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=369,
  serialized_end=410,
)


_DIRECTIONANDDEPTH = _descriptor.Descriptor(
  name='DirectionAndDepth',
  full_name='DirectionAndDepth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='u', full_name='DirectionAndDepth.u', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v', full_name='DirectionAndDepth.v', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='DirectionAndDepth.w', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='d', full_name='DirectionAndDepth.d', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=412,
  serialized_end=475,
)


_POINTS = _descriptor.Descriptor(
  name='Points',
  full_name='Points',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='Points.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=477,
  serialized_end=521,
)

_TRANSFORMPROTO.fields_by_name['c1'].message_type = _FLOAT4PROTO
_TRANSFORMPROTO.fields_by_name['c2'].message_type = _FLOAT4PROTO
_TRANSFORMPROTO.fields_by_name['c3'].message_type = _FLOAT4PROTO
_TRANSFORMPROTO.fields_by_name['c4'].message_type = _FLOAT4PROTO
_MESHPROTO.fields_by_name['vertices'].message_type = _VERTEXPROTO
_MESHPROTO.fields_by_name['transform'].message_type = _TRANSFORMPROTO
_MESHESPROTO.fields_by_name['meshes'].message_type = _MESHPROTO
_POINTS.fields_by_name['points'].message_type = _DIRECTIONANDDEPTH
DESCRIPTOR.message_types_by_name['Float4Proto'] = _FLOAT4PROTO
DESCRIPTOR.message_types_by_name['TransformProto'] = _TRANSFORMPROTO
DESCRIPTOR.message_types_by_name['VertexProto'] = _VERTEXPROTO
DESCRIPTOR.message_types_by_name['MeshProto'] = _MESHPROTO
DESCRIPTOR.message_types_by_name['MeshesProto'] = _MESHESPROTO
DESCRIPTOR.message_types_by_name['DirectionAndDepth'] = _DIRECTIONANDDEPTH
DESCRIPTOR.message_types_by_name['Points'] = _POINTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Float4Proto = _reflection.GeneratedProtocolMessageType('Float4Proto', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT4PROTO,
  '__module__' : 'Mesh_pb2'
  # @@protoc_insertion_point(class_scope:Float4Proto)
  })
_sym_db.RegisterMessage(Float4Proto)

TransformProto = _reflection.GeneratedProtocolMessageType('TransformProto', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMPROTO,
  '__module__' : 'Mesh_pb2'
  # @@protoc_insertion_point(class_scope:TransformProto)
  })
_sym_db.RegisterMessage(TransformProto)

VertexProto = _reflection.GeneratedProtocolMessageType('VertexProto', (_message.Message,), {
  'DESCRIPTOR' : _VERTEXPROTO,
  '__module__' : 'Mesh_pb2'
  # @@protoc_insertion_point(class_scope:VertexProto)
  })
_sym_db.RegisterMessage(VertexProto)

MeshProto = _reflection.GeneratedProtocolMessageType('MeshProto', (_message.Message,), {
  'DESCRIPTOR' : _MESHPROTO,
  '__module__' : 'Mesh_pb2'
  # @@protoc_insertion_point(class_scope:MeshProto)
  })
_sym_db.RegisterMessage(MeshProto)

MeshesProto = _reflection.GeneratedProtocolMessageType('MeshesProto', (_message.Message,), {
  'DESCRIPTOR' : _MESHESPROTO,
  '__module__' : 'Mesh_pb2'
  # @@protoc_insertion_point(class_scope:MeshesProto)
  })
_sym_db.RegisterMessage(MeshesProto)

DirectionAndDepth = _reflection.GeneratedProtocolMessageType('DirectionAndDepth', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTIONANDDEPTH,
  '__module__' : 'Mesh_pb2'
  # @@protoc_insertion_point(class_scope:DirectionAndDepth)
  })
_sym_db.RegisterMessage(DirectionAndDepth)

Points = _reflection.GeneratedProtocolMessageType('Points', (_message.Message,), {
  'DESCRIPTOR' : _POINTS,
  '__module__' : 'Mesh_pb2'
  # @@protoc_insertion_point(class_scope:Points)
  })
_sym_db.RegisterMessage(Points)


# @@protoc_insertion_point(module_scope)
