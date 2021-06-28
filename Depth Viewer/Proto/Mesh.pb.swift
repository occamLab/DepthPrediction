// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: Mesh.proto
//
// For information on using the generated types, please see the documentation:
//   https://github.com/apple/swift-protobuf/

import Foundation
import SwiftProtobuf

// If the compiler emits an error on this type, it is because this file
// was generated by a version of the `protoc` Swift plug-in that is
// incompatible with the version of SwiftProtobuf to which you are linking.
// Please ensure that you are building against the same version of the API
// that was used to generate this file.
fileprivate struct _GeneratedWithProtocGenSwiftVersion: SwiftProtobuf.ProtobufAPIVersionCheck {
  struct _2: SwiftProtobuf.ProtobufAPIVersion_2 {}
  typealias Version = _2
}

struct Float4Proto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var x: Float = 0

  var y: Float = 0

  var z: Float = 0

  var w: Float = 0

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct TransformProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var c1: Float4Proto {
    get {return _c1 ?? Float4Proto()}
    set {_c1 = newValue}
  }
  /// Returns true if `c1` has been explicitly set.
  var hasC1: Bool {return self._c1 != nil}
  /// Clears the value of `c1`. Subsequent reads from it will return its default value.
  mutating func clearC1() {self._c1 = nil}

  var c2: Float4Proto {
    get {return _c2 ?? Float4Proto()}
    set {_c2 = newValue}
  }
  /// Returns true if `c2` has been explicitly set.
  var hasC2: Bool {return self._c2 != nil}
  /// Clears the value of `c2`. Subsequent reads from it will return its default value.
  mutating func clearC2() {self._c2 = nil}

  var c3: Float4Proto {
    get {return _c3 ?? Float4Proto()}
    set {_c3 = newValue}
  }
  /// Returns true if `c3` has been explicitly set.
  var hasC3: Bool {return self._c3 != nil}
  /// Clears the value of `c3`. Subsequent reads from it will return its default value.
  mutating func clearC3() {self._c3 = nil}

  var c4: Float4Proto {
    get {return _c4 ?? Float4Proto()}
    set {_c4 = newValue}
  }
  /// Returns true if `c4` has been explicitly set.
  var hasC4: Bool {return self._c4 != nil}
  /// Clears the value of `c4`. Subsequent reads from it will return its default value.
  mutating func clearC4() {self._c4 = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _c1: Float4Proto? = nil
  fileprivate var _c2: Float4Proto? = nil
  fileprivate var _c3: Float4Proto? = nil
  fileprivate var _c4: Float4Proto? = nil
}

struct VertexProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var x: Float = 0

  var y: Float = 0

  var z: Float = 0

  var u: Float = 0

  var v: Float = 0

  var w: Float = 0

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct MeshProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var vertices: [VertexProto] = []

  var transform: TransformProto {
    get {return _transform ?? TransformProto()}
    set {_transform = newValue}
  }
  /// Returns true if `transform` has been explicitly set.
  var hasTransform: Bool {return self._transform != nil}
  /// Clears the value of `transform`. Subsequent reads from it will return its default value.
  mutating func clearTransform() {self._transform = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _transform: TransformProto? = nil
}

struct MeshesProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var meshes: [MeshProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension Float4Proto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "Float4Proto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "x"),
    2: .same(proto: "y"),
    3: .same(proto: "z"),
    4: .same(proto: "w"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      switch fieldNumber {
      case 1: try decoder.decodeSingularFloatField(value: &self.x)
      case 2: try decoder.decodeSingularFloatField(value: &self.y)
      case 3: try decoder.decodeSingularFloatField(value: &self.z)
      case 4: try decoder.decodeSingularFloatField(value: &self.w)
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if self.x != 0 {
      try visitor.visitSingularFloatField(value: self.x, fieldNumber: 1)
    }
    if self.y != 0 {
      try visitor.visitSingularFloatField(value: self.y, fieldNumber: 2)
    }
    if self.z != 0 {
      try visitor.visitSingularFloatField(value: self.z, fieldNumber: 3)
    }
    if self.w != 0 {
      try visitor.visitSingularFloatField(value: self.w, fieldNumber: 4)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: Float4Proto, rhs: Float4Proto) -> Bool {
    if lhs.x != rhs.x {return false}
    if lhs.y != rhs.y {return false}
    if lhs.z != rhs.z {return false}
    if lhs.w != rhs.w {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension TransformProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "TransformProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "c1"),
    2: .same(proto: "c2"),
    3: .same(proto: "c3"),
    4: .same(proto: "c4"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      switch fieldNumber {
      case 1: try decoder.decodeSingularMessageField(value: &self._c1)
      case 2: try decoder.decodeSingularMessageField(value: &self._c2)
      case 3: try decoder.decodeSingularMessageField(value: &self._c3)
      case 4: try decoder.decodeSingularMessageField(value: &self._c4)
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if let v = self._c1 {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    }
    if let v = self._c2 {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    }
    if let v = self._c3 {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 3)
    }
    if let v = self._c4 {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 4)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: TransformProto, rhs: TransformProto) -> Bool {
    if lhs._c1 != rhs._c1 {return false}
    if lhs._c2 != rhs._c2 {return false}
    if lhs._c3 != rhs._c3 {return false}
    if lhs._c4 != rhs._c4 {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension VertexProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "VertexProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "x"),
    2: .same(proto: "y"),
    3: .same(proto: "z"),
    4: .same(proto: "u"),
    5: .same(proto: "v"),
    6: .same(proto: "w"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      switch fieldNumber {
      case 1: try decoder.decodeSingularFloatField(value: &self.x)
      case 2: try decoder.decodeSingularFloatField(value: &self.y)
      case 3: try decoder.decodeSingularFloatField(value: &self.z)
      case 4: try decoder.decodeSingularFloatField(value: &self.u)
      case 5: try decoder.decodeSingularFloatField(value: &self.v)
      case 6: try decoder.decodeSingularFloatField(value: &self.w)
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if self.x != 0 {
      try visitor.visitSingularFloatField(value: self.x, fieldNumber: 1)
    }
    if self.y != 0 {
      try visitor.visitSingularFloatField(value: self.y, fieldNumber: 2)
    }
    if self.z != 0 {
      try visitor.visitSingularFloatField(value: self.z, fieldNumber: 3)
    }
    if self.u != 0 {
      try visitor.visitSingularFloatField(value: self.u, fieldNumber: 4)
    }
    if self.v != 0 {
      try visitor.visitSingularFloatField(value: self.v, fieldNumber: 5)
    }
    if self.w != 0 {
      try visitor.visitSingularFloatField(value: self.w, fieldNumber: 6)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: VertexProto, rhs: VertexProto) -> Bool {
    if lhs.x != rhs.x {return false}
    if lhs.y != rhs.y {return false}
    if lhs.z != rhs.z {return false}
    if lhs.u != rhs.u {return false}
    if lhs.v != rhs.v {return false}
    if lhs.w != rhs.w {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension MeshProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "MeshProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "vertices"),
    2: .same(proto: "transform"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      switch fieldNumber {
      case 1: try decoder.decodeRepeatedMessageField(value: &self.vertices)
      case 2: try decoder.decodeSingularMessageField(value: &self._transform)
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.vertices.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.vertices, fieldNumber: 1)
    }
    if let v = self._transform {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: MeshProto, rhs: MeshProto) -> Bool {
    if lhs.vertices != rhs.vertices {return false}
    if lhs._transform != rhs._transform {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension MeshesProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "MeshesProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "meshes"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      switch fieldNumber {
      case 1: try decoder.decodeRepeatedMessageField(value: &self.meshes)
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.meshes.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.meshes, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: MeshesProto, rhs: MeshesProto) -> Bool {
    if lhs.meshes != rhs.meshes {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
