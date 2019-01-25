// Generated by the Scala Plugin for the Protocol Buffer Compiler.
// Do not edit!
//
// Protofile syntax: PROTO3

package tech.sourced.featurext.generated.service

object ServiceProto extends _root_.scalapb.GeneratedFileObject {
  lazy val dependencies: Seq[_root_.scalapb.GeneratedFileObject] = Seq(
    com.google.protobuf.gogo.GogoProto,
    gopkg.in.bblfsh.sdk.v1.uast.generated.GeneratedProto
  )
  lazy val messagesCompanions: Seq[_root_.scalapb.GeneratedMessageCompanion[_]] = Seq(
    tech.sourced.featurext.generated.service.IdentifiersOptions,
    tech.sourced.featurext.generated.service.LiteralsOptions,
    tech.sourced.featurext.generated.service.Uast2seqOptions,
    tech.sourced.featurext.generated.service.GraphletOptions,
    tech.sourced.featurext.generated.service.ExtractRequest,
    tech.sourced.featurext.generated.service.IdentifiersRequest,
    tech.sourced.featurext.generated.service.LiteralsRequest,
    tech.sourced.featurext.generated.service.Uast2seqRequest,
    tech.sourced.featurext.generated.service.GraphletRequest,
    tech.sourced.featurext.generated.service.Feature,
    tech.sourced.featurext.generated.service.FeaturesReply
  )
  private lazy val ProtoBytes: Array[Byte] =
      scalapb.Encoding.fromBase64(scala.collection.Seq(
  """Cg1zZXJ2aWNlLnByb3RvEiB0ZWNoLnNvdXJjZWQuZmVhdHVyZXh0LmdlbmVyYXRlZBotZ2l0aHViLmNvbS9nb2dvL3Byb3RvY
  nVmL2dvZ29wcm90by9nb2dvLnByb3RvGitnb3BrZy5pbi9iYmxmc2gvc2RrLnYxL3Vhc3QvZ2VuZXJhdGVkLnByb3RvInYKEklkZ
  W50aWZpZXJzT3B0aW9ucxIqChBkb2NmcmVxVGhyZXNob2xkGAEgASgFUhBkb2NmcmVxVGhyZXNob2xkEhYKBndlaWdodBgCIAEoB
  VIGd2VpZ2h0EhwKCXNwbGl0U3RlbRgDIAEoCFIJc3BsaXRTdGVtIlUKD0xpdGVyYWxzT3B0aW9ucxIqChBkb2NmcmVxVGhyZXNob
  2xkGAEgASgFUhBkb2NmcmVxVGhyZXNob2xkEhYKBndlaWdodBgCIAEoBVIGd2VpZ2h0IoUBCg9VYXN0MnNlcU9wdGlvbnMSKgoQZ
  G9jZnJlcVRocmVzaG9sZBgBIAEoBVIQZG9jZnJlcVRocmVzaG9sZBIWCgZ3ZWlnaHQYAiABKAVSBndlaWdodBIWCgZzdHJpZGUYA
  yABKAVSBnN0cmlkZRIWCgZzZXFMZW4YBCADKAVSBnNlcUxlbiJVCg9HcmFwaGxldE9wdGlvbnMSKgoQZG9jZnJlcVRocmVzaG9sZ
  BgBIAEoBVIQZG9jZnJlcVRocmVzaG9sZBIWCgZ3ZWlnaHQYAiABKAVSBndlaWdodCKMAwoORXh0cmFjdFJlcXVlc3QSNQoEdWFzd
  BgBIAEoCzIhLmdvcGtnLmluLmJibGZzaC5zZGsudjEudWFzdC5Ob2RlUgR1YXN0ElYKC2lkZW50aWZpZXJzGAIgASgLMjQudGVja
  C5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuSWRlbnRpZmllcnNPcHRpb25zUgtpZGVudGlmaWVycxJNCghsaXRlcmFscxgDI
  AEoCzIxLnRlY2guc291cmNlZC5mZWF0dXJleHQuZ2VuZXJhdGVkLkxpdGVyYWxzT3B0aW9uc1IIbGl0ZXJhbHMSTQoIdWFzdDJzZ
  XEYBCABKAsyMS50ZWNoLnNvdXJjZWQuZmVhdHVyZXh0LmdlbmVyYXRlZC5VYXN0MnNlcU9wdGlvbnNSCHVhc3Qyc2VxEk0KCGdyY
  XBobGV0GAUgASgLMjEudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuR3JhcGhsZXRPcHRpb25zUghncmFwaGxldCKbA
  QoSSWRlbnRpZmllcnNSZXF1ZXN0EjUKBHVhc3QYASABKAsyIS5nb3BrZy5pbi5iYmxmc2guc2RrLnYxLnVhc3QuTm9kZVIEdWFzd
  BJOCgdvcHRpb25zGAIgASgLMjQudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuSWRlbnRpZmllcnNPcHRpb25zUgdvc
  HRpb25zIpUBCg9MaXRlcmFsc1JlcXVlc3QSNQoEdWFzdBgBIAEoCzIhLmdvcGtnLmluLmJibGZzaC5zZGsudjEudWFzdC5Ob2RlU
  gR1YXN0EksKB29wdGlvbnMYAiABKAsyMS50ZWNoLnNvdXJjZWQuZmVhdHVyZXh0LmdlbmVyYXRlZC5MaXRlcmFsc09wdGlvbnNSB
  29wdGlvbnMilQEKD1Vhc3Qyc2VxUmVxdWVzdBI1CgR1YXN0GAEgASgLMiEuZ29wa2cuaW4uYmJsZnNoLnNkay52MS51YXN0Lk5vZ
  GVSBHVhc3QSSwoHb3B0aW9ucxgCIAEoCzIxLnRlY2guc291cmNlZC5mZWF0dXJleHQuZ2VuZXJhdGVkLlVhc3Qyc2VxT3B0aW9uc
  1IHb3B0aW9ucyKVAQoPR3JhcGhsZXRSZXF1ZXN0EjUKBHVhc3QYASABKAsyIS5nb3BrZy5pbi5iYmxmc2guc2RrLnYxLnVhc3QuT
  m9kZVIEdWFzdBJLCgdvcHRpb25zGAIgASgLMjEudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuR3JhcGhsZXRPcHRpb
  25zUgdvcHRpb25zIjUKB0ZlYXR1cmUSEgoEbmFtZRgBIAEoCVIEbmFtZRIWCgZ3ZWlnaHQYAiABKAJSBndlaWdodCJWCg1GZWF0d
  XJlc1JlcGx5EkUKCGZlYXR1cmVzGAEgAygLMikudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuRmVhdHVyZVIIZmVhd
  HVyZXMy0AQKEEZlYXR1cmVFeHRyYWN0b3ISbgoHRXh0cmFjdBIwLnRlY2guc291cmNlZC5mZWF0dXJleHQuZ2VuZXJhdGVkLkV4d
  HJhY3RSZXF1ZXN0Gi8udGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuRmVhdHVyZXNSZXBseSIAEnYKC0lkZW50aWZpZ
  XJzEjQudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuSWRlbnRpZmllcnNSZXF1ZXN0Gi8udGVjaC5zb3VyY2VkLmZlY
  XR1cmV4dC5nZW5lcmF0ZWQuRmVhdHVyZXNSZXBseSIAEnAKCExpdGVyYWxzEjEudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lc
  mF0ZWQuTGl0ZXJhbHNSZXF1ZXN0Gi8udGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuRmVhdHVyZXNSZXBseSIAEnAKC
  FVhc3Qyc2VxEjEudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuVWFzdDJzZXFSZXF1ZXN0Gi8udGVjaC5zb3VyY2VkL
  mZlYXR1cmV4dC5nZW5lcmF0ZWQuRmVhdHVyZXNSZXBseSIAEnAKCEdyYXBobGV0EjEudGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZ
  W5lcmF0ZWQuR3JhcGhsZXRSZXF1ZXN0Gi8udGVjaC5zb3VyY2VkLmZlYXR1cmV4dC5nZW5lcmF0ZWQuRmVhdHVyZXNSZXBseSIAY
  gZwcm90bzM="""
      ).mkString)
  lazy val scalaDescriptor: _root_.scalapb.descriptors.FileDescriptor = {
    val scalaProto = com.google.protobuf.descriptor.FileDescriptorProto.parseFrom(ProtoBytes)
    _root_.scalapb.descriptors.FileDescriptor.buildFrom(scalaProto, dependencies.map(_.scalaDescriptor))
  }
  lazy val javaDescriptor: com.google.protobuf.Descriptors.FileDescriptor = {
    val javaProto = com.google.protobuf.DescriptorProtos.FileDescriptorProto.parseFrom(ProtoBytes)
    com.google.protobuf.Descriptors.FileDescriptor.buildFrom(javaProto, Array(
      com.google.protobuf.gogo.GogoProto.javaDescriptor,
      gopkg.in.bblfsh.sdk.v1.uast.generated.GeneratedProto.javaDescriptor
    ))
  }
  @deprecated("Use javaDescriptor instead. In a future version this will refer to scalaDescriptor.", "ScalaPB 0.5.47")
  def descriptor: com.google.protobuf.Descriptors.FileDescriptor = javaDescriptor
}