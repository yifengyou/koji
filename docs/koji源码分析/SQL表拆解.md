# koji-hub SQL表拆解

## 基本信息

* 显示所有数据库

```
su - koji -c "psql koji koji -c '\l'"
                              List of databases
   Name    |  Owner   | Encoding | Collate |  Ctype  |   Access privileges   
-----------+----------+----------+---------+---------+-----------------------
 koji      | koji     | UTF8     | C.UTF-8 | C.UTF-8 |
 postgres  | postgres | UTF8     | C.UTF-8 | C.UTF-8 |
 template0 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
           |          |          |         |         | postgres=CTc/postgres
 template1 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
           |          |          |         |         | postgres=CTc/postgres
(4 rows)
```

* 显示koji用户所有数据库表

```
su - koji -c "psql koji koji -c '\dt'"
                 List of relations
 Schema |           Name            | Type  | Owner
--------+---------------------------+-------+-------
 public | archive_components        | table | koji
 public | archive_rpm_components    | table | koji
 public | archiveinfo               | table | koji
 public | archivetypes              | table | koji
 public | btype                     | table | koji
 public | build                     | table | koji
 public | build_notifications       | table | koji
 public | build_notifications_block | table | koji
 public | build_reservations        | table | koji
 public | build_target              | table | koji
 public | build_target_config       | table | koji
 public | build_types               | table | koji
 public | buildroot                 | table | koji
 public | buildroot_archives        | table | koji
 public | buildroot_listing         | table | koji
 public | buildroot_tools_info      | table | koji
 public | cg_users                  | table | koji
 public | channels                  | table | koji
 public | content_generator         | table | koji
 public | event_labels              | table | koji
 public | events                    | table | koji
 public | external_repo             | table | koji
 public | external_repo_config      | table | koji
 public | group_config              | table | koji
 public | group_package_listing     | table | koji
 public | group_req_listing         | table | koji
 public | groups                    | table | koji
 public | host                      | table | koji
 public | host_channels             | table | koji
 public | host_config               | table | koji
 public | image_archives            | table | koji
 public | image_builds              | table | koji
 public | maven_archives            | table | koji
 public | maven_builds              | table | koji
 public | package                   | table | koji
 public | permissions               | table | koji
 public | proton_queue              | table | koji
 public | repo                      | table | koji
 public | rpminfo                   | table | koji
 public | rpmsigs                   | table | koji
 public | sessions                  | table | koji
 public | standard_buildroot        | table | koji
 public | tag                       | table | koji
 public | tag_config                | table | koji
 public | tag_external_repos        | table | koji
 public | tag_extra                 | table | koji
 public | tag_inheritance           | table | koji
 public | tag_listing               | table | koji
 public | tag_package_owners        | table | koji
 public | tag_packages              | table | koji
 public | tag_updates               | table | koji
 public | task                      | table | koji
 public | user_groups               | table | koji
 public | user_krb_principals       | table | koji
 public | user_perms                | table | koji
 public | users                     | table | koji
 public | volume                    | table | koji
 public | win_archives              | table | koji
 public | win_builds                | table | koji
(59 rows)

```

## 外部访问POSTGRESQL

![20221126_111049_15](image/20221126_111049_15.png)

![20221126_111113_21](image/20221126_111113_21.png)

![20221126_111134_37](image/20221126_111134_37.png)

![20221126_111141_11](image/20221126_111141_11.png)

![20221126_111337_94](image/20221126_111337_94.png)

![20221126_111507_82](image/20221126_111507_82.png)

![20221126_111516_45](image/20221126_111516_45.png)

![20221126_111538_84](image/20221126_111538_84.png)

![20221126_111606_80](image/20221126_111606_80.png)

## SQL表

```
/*
 Navicat Premium Data Transfer

 Source Server         : koji
 Source Server Type    : PostgreSQL
 Source Server Version : 100021
 Source Host           : 192.168.33.61:5432
 Source Catalog        : koji
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100021
 File Encoding         : 65001

 Date: 26/11/2022 11:30:58
*/


-- ----------------------------
-- Sequence structure for archiveinfo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."archiveinfo_id_seq";
CREATE SEQUENCE "public"."archiveinfo_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for archivetypes_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."archivetypes_id_seq";
CREATE SEQUENCE "public"."archivetypes_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for btype_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."btype_id_seq";
CREATE SEQUENCE "public"."btype_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for build_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."build_id_seq";
CREATE SEQUENCE "public"."build_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for build_notifications_block_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."build_notifications_block_id_seq";
CREATE SEQUENCE "public"."build_notifications_block_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for build_notifications_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."build_notifications_id_seq";
CREATE SEQUENCE "public"."build_notifications_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for build_target_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."build_target_id_seq";
CREATE SEQUENCE "public"."build_target_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for buildroot_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."buildroot_id_seq";
CREATE SEQUENCE "public"."buildroot_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for channels_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."channels_id_seq";
CREATE SEQUENCE "public"."channels_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for content_generator_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."content_generator_id_seq";
CREATE SEQUENCE "public"."content_generator_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for events_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."events_id_seq";
CREATE SEQUENCE "public"."events_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for external_repo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."external_repo_id_seq";
CREATE SEQUENCE "public"."external_repo_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for groups_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."groups_id_seq";
CREATE SEQUENCE "public"."groups_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for host_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."host_id_seq";
CREATE SEQUENCE "public"."host_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for package_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."package_id_seq";
CREATE SEQUENCE "public"."package_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for permissions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."permissions_id_seq";
CREATE SEQUENCE "public"."permissions_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for proton_queue_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."proton_queue_id_seq";
CREATE SEQUENCE "public"."proton_queue_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for repo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."repo_id_seq";
CREATE SEQUENCE "public"."repo_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for rpminfo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."rpminfo_id_seq";
CREATE SEQUENCE "public"."rpminfo_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for sessions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."sessions_id_seq";
CREATE SEQUENCE "public"."sessions_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tag_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tag_id_seq";
CREATE SEQUENCE "public"."tag_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tag_updates_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tag_updates_id_seq";
CREATE SEQUENCE "public"."tag_updates_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for task_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."task_id_seq";
CREATE SEQUENCE "public"."task_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for users_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."users_id_seq";
CREATE SEQUENCE "public"."users_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for volume_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."volume_id_seq";
CREATE SEQUENCE "public"."volume_id_seq"
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Table structure for archive_components
-- ----------------------------
DROP TABLE IF EXISTS "public"."archive_components";
CREATE TABLE "public"."archive_components" (
  "archive_id" int4 NOT NULL,
  "component_id" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for archive_rpm_components
-- ----------------------------
DROP TABLE IF EXISTS "public"."archive_rpm_components";
CREATE TABLE "public"."archive_rpm_components" (
  "archive_id" int4 NOT NULL,
  "rpm_id" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for archiveinfo
-- ----------------------------
DROP TABLE IF EXISTS "public"."archiveinfo";
CREATE TABLE "public"."archiveinfo" (
  "id" int4 NOT NULL DEFAULT nextval('archiveinfo_id_seq'::regclass),
  "type_id" int4 NOT NULL,
  "btype_id" int4,
  "build_id" int4 NOT NULL,
  "buildroot_id" int4,
  "filename" text COLLATE "pg_catalog"."default" NOT NULL,
  "size" int8 NOT NULL,
  "checksum" text COLLATE "pg_catalog"."default" NOT NULL,
  "checksum_type" int4 NOT NULL,
  "metadata_only" bool NOT NULL DEFAULT false,
  "extra" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for archivetypes
-- ----------------------------
DROP TABLE IF EXISTS "public"."archivetypes";
CREATE TABLE "public"."archivetypes" (
  "id" int4 NOT NULL DEFAULT nextval('archivetypes_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL,
  "description" text COLLATE "pg_catalog"."default" NOT NULL,
  "extensions" text COLLATE "pg_catalog"."default" NOT NULL,
  "compression_type" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for btype
-- ----------------------------
DROP TABLE IF EXISTS "public"."btype";
CREATE TABLE "public"."btype" (
  "id" int4 NOT NULL DEFAULT nextval('btype_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for build
-- ----------------------------
DROP TABLE IF EXISTS "public"."build";
CREATE TABLE "public"."build" (
  "id" int4 NOT NULL DEFAULT nextval('build_id_seq'::regclass),
  "volume_id" int4 NOT NULL,
  "pkg_id" int4 NOT NULL,
  "version" text COLLATE "pg_catalog"."default" NOT NULL,
  "release" text COLLATE "pg_catalog"."default" NOT NULL,
  "epoch" int4,
  "source" text COLLATE "pg_catalog"."default",
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "start_time" timestamptz(6),
  "completion_time" timestamptz(6),
  "state" int4 NOT NULL,
  "task_id" int4,
  "owner" int4 NOT NULL,
  "cg_id" int4,
  "extra" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for build_notifications
-- ----------------------------
DROP TABLE IF EXISTS "public"."build_notifications";
CREATE TABLE "public"."build_notifications" (
  "id" int4 NOT NULL DEFAULT nextval('build_notifications_id_seq'::regclass),
  "user_id" int4 NOT NULL,
  "package_id" int4,
  "tag_id" int4,
  "success_only" bool NOT NULL DEFAULT false,
  "email" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for build_notifications_block
-- ----------------------------
DROP TABLE IF EXISTS "public"."build_notifications_block";
CREATE TABLE "public"."build_notifications_block" (
  "id" int4 NOT NULL DEFAULT nextval('build_notifications_block_id_seq'::regclass),
  "user_id" int4 NOT NULL,
  "package_id" int4,
  "tag_id" int4
)
;

-- ----------------------------
-- Table structure for build_reservations
-- ----------------------------
DROP TABLE IF EXISTS "public"."build_reservations";
CREATE TABLE "public"."build_reservations" (
  "build_id" int4 NOT NULL,
  "token" varchar(64) COLLATE "pg_catalog"."default",
  "created" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Table structure for build_target
-- ----------------------------
DROP TABLE IF EXISTS "public"."build_target";
CREATE TABLE "public"."build_target" (
  "id" int4 NOT NULL DEFAULT nextval('build_target_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for build_target_config
-- ----------------------------
DROP TABLE IF EXISTS "public"."build_target_config";
CREATE TABLE "public"."build_target_config" (
  "build_target_id" int4 NOT NULL,
  "build_tag" int4 NOT NULL,
  "dest_tag" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for build_types
-- ----------------------------
DROP TABLE IF EXISTS "public"."build_types";
CREATE TABLE "public"."build_types" (
  "build_id" int4 NOT NULL,
  "btype_id" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for buildroot
-- ----------------------------
DROP TABLE IF EXISTS "public"."buildroot";
CREATE TABLE "public"."buildroot" (
  "id" int4 NOT NULL DEFAULT nextval('buildroot_id_seq'::regclass),
  "br_type" int4 NOT NULL,
  "cg_id" int4,
  "cg_version" text COLLATE "pg_catalog"."default",
  "container_type" text COLLATE "pg_catalog"."default",
  "container_arch" text COLLATE "pg_catalog"."default",
  "host_os" text COLLATE "pg_catalog"."default",
  "host_arch" text COLLATE "pg_catalog"."default",
  "extra" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for buildroot_archives
-- ----------------------------
DROP TABLE IF EXISTS "public"."buildroot_archives";
CREATE TABLE "public"."buildroot_archives" (
  "buildroot_id" int4 NOT NULL,
  "archive_id" int4 NOT NULL,
  "project_dep" bool NOT NULL
)
;

-- ----------------------------
-- Table structure for buildroot_listing
-- ----------------------------
DROP TABLE IF EXISTS "public"."buildroot_listing";
CREATE TABLE "public"."buildroot_listing" (
  "buildroot_id" int4 NOT NULL,
  "rpm_id" int4 NOT NULL,
  "is_update" bool NOT NULL DEFAULT false
)
;

-- ----------------------------
-- Table structure for buildroot_tools_info
-- ----------------------------
DROP TABLE IF EXISTS "public"."buildroot_tools_info";
CREATE TABLE "public"."buildroot_tools_info" (
  "buildroot_id" int4 NOT NULL,
  "tool" text COLLATE "pg_catalog"."default" NOT NULL,
  "version" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for cg_users
-- ----------------------------
DROP TABLE IF EXISTS "public"."cg_users";
CREATE TABLE "public"."cg_users" (
  "cg_id" int4 NOT NULL,
  "user_id" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for channels
-- ----------------------------
DROP TABLE IF EXISTS "public"."channels";
CREATE TABLE "public"."channels" (
  "id" int4 NOT NULL DEFAULT nextval('channels_id_seq'::regclass),
  "name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "description" text COLLATE "pg_catalog"."default",
  "enabled" bool NOT NULL DEFAULT true,
  "comment" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for content_generator
-- ----------------------------
DROP TABLE IF EXISTS "public"."content_generator";
CREATE TABLE "public"."content_generator" (
  "id" int4 NOT NULL DEFAULT nextval('content_generator_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for event_labels
-- ----------------------------
DROP TABLE IF EXISTS "public"."event_labels";
CREATE TABLE "public"."event_labels" (
  "event_id" int4 NOT NULL,
  "label" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for events
-- ----------------------------
DROP TABLE IF EXISTS "public"."events";
CREATE TABLE "public"."events" (
  "id" int4 NOT NULL DEFAULT nextval('events_id_seq'::regclass),
  "time" timestamptz(6) NOT NULL DEFAULT clock_timestamp()
)
;

-- ----------------------------
-- Table structure for external_repo
-- ----------------------------
DROP TABLE IF EXISTS "public"."external_repo";
CREATE TABLE "public"."external_repo" (
  "id" int4 NOT NULL DEFAULT nextval('external_repo_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for external_repo_config
-- ----------------------------
DROP TABLE IF EXISTS "public"."external_repo_config";
CREATE TABLE "public"."external_repo_config" (
  "external_repo_id" int4 NOT NULL,
  "url" text COLLATE "pg_catalog"."default" NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for group_config
-- ----------------------------
DROP TABLE IF EXISTS "public"."group_config";
CREATE TABLE "public"."group_config" (
  "group_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL,
  "blocked" bool NOT NULL DEFAULT false,
  "exported" bool DEFAULT true,
  "display_name" text COLLATE "pg_catalog"."default" NOT NULL,
  "is_default" bool,
  "uservisible" bool,
  "description" text COLLATE "pg_catalog"."default",
  "langonly" text COLLATE "pg_catalog"."default",
  "biarchonly" bool,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for group_package_listing
-- ----------------------------
DROP TABLE IF EXISTS "public"."group_package_listing";
CREATE TABLE "public"."group_package_listing" (
  "group_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL,
  "package" text COLLATE "pg_catalog"."default" NOT NULL,
  "blocked" bool NOT NULL DEFAULT false,
  "type" varchar(25) COLLATE "pg_catalog"."default" NOT NULL,
  "basearchonly" bool,
  "requires" text COLLATE "pg_catalog"."default",
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for group_req_listing
-- ----------------------------
DROP TABLE IF EXISTS "public"."group_req_listing";
CREATE TABLE "public"."group_req_listing" (
  "group_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL,
  "req_id" int4 NOT NULL,
  "blocked" bool NOT NULL DEFAULT false,
  "type" varchar(25) COLLATE "pg_catalog"."default",
  "is_metapkg" bool NOT NULL DEFAULT false,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for groups
-- ----------------------------
DROP TABLE IF EXISTS "public"."groups";
CREATE TABLE "public"."groups" (
  "id" int4 NOT NULL DEFAULT nextval('groups_id_seq'::regclass),
  "name" varchar(50) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for host
-- ----------------------------
DROP TABLE IF EXISTS "public"."host";
CREATE TABLE "public"."host" (
  "id" int4 NOT NULL DEFAULT nextval('host_id_seq'::regclass),
  "user_id" int4 NOT NULL,
  "name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "task_load" float8 NOT NULL DEFAULT 0.0,
  "ready" bool NOT NULL DEFAULT false
)
;

-- ----------------------------
-- Table structure for host_channels
-- ----------------------------
DROP TABLE IF EXISTS "public"."host_channels";
CREATE TABLE "public"."host_channels" (
  "host_id" int4 NOT NULL,
  "channel_id" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for host_config
-- ----------------------------
DROP TABLE IF EXISTS "public"."host_config";
CREATE TABLE "public"."host_config" (
  "host_id" int4 NOT NULL,
  "arches" text COLLATE "pg_catalog"."default",
  "capacity" float8 NOT NULL DEFAULT 2.0,
  "description" text COLLATE "pg_catalog"."default",
  "comment" text COLLATE "pg_catalog"."default",
  "enabled" bool NOT NULL DEFAULT true,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for image_archives
-- ----------------------------
DROP TABLE IF EXISTS "public"."image_archives";
CREATE TABLE "public"."image_archives" (
  "archive_id" int4 NOT NULL,
  "arch" varchar(16) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for image_builds
-- ----------------------------
DROP TABLE IF EXISTS "public"."image_builds";
CREATE TABLE "public"."image_builds" (
  "build_id" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for maven_archives
-- ----------------------------
DROP TABLE IF EXISTS "public"."maven_archives";
CREATE TABLE "public"."maven_archives" (
  "archive_id" int4 NOT NULL,
  "group_id" text COLLATE "pg_catalog"."default" NOT NULL,
  "artifact_id" text COLLATE "pg_catalog"."default" NOT NULL,
  "version" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for maven_builds
-- ----------------------------
DROP TABLE IF EXISTS "public"."maven_builds";
CREATE TABLE "public"."maven_builds" (
  "build_id" int4 NOT NULL,
  "group_id" text COLLATE "pg_catalog"."default" NOT NULL,
  "artifact_id" text COLLATE "pg_catalog"."default" NOT NULL,
  "version" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for package
-- ----------------------------
DROP TABLE IF EXISTS "public"."package";
CREATE TABLE "public"."package" (
  "id" int4 NOT NULL DEFAULT nextval('package_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for permissions
-- ----------------------------
DROP TABLE IF EXISTS "public"."permissions";
CREATE TABLE "public"."permissions" (
  "id" int4 NOT NULL DEFAULT nextval('permissions_id_seq'::regclass),
  "name" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "description" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for proton_queue
-- ----------------------------
DROP TABLE IF EXISTS "public"."proton_queue";
CREATE TABLE "public"."proton_queue" (
  "id" int4 NOT NULL DEFAULT nextval('proton_queue_id_seq'::regclass),
  "created_ts" timestamptz(6) DEFAULT now(),
  "address" text COLLATE "pg_catalog"."default" NOT NULL,
  "props" json NOT NULL,
  "body" json NOT NULL
)
;

-- ----------------------------
-- Table structure for repo
-- ----------------------------
DROP TABLE IF EXISTS "public"."repo";
CREATE TABLE "public"."repo" (
  "id" int4 NOT NULL DEFAULT nextval('repo_id_seq'::regclass),
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "tag_id" int4 NOT NULL,
  "state" int4,
  "dist" bool DEFAULT false,
  "task_id" int4
)
;

-- ----------------------------
-- Table structure for rpminfo
-- ----------------------------
DROP TABLE IF EXISTS "public"."rpminfo";
CREATE TABLE "public"."rpminfo" (
  "id" int4 NOT NULL DEFAULT nextval('rpminfo_id_seq'::regclass),
  "build_id" int4,
  "buildroot_id" int4,
  "name" text COLLATE "pg_catalog"."default" NOT NULL,
  "version" text COLLATE "pg_catalog"."default" NOT NULL,
  "release" text COLLATE "pg_catalog"."default" NOT NULL,
  "epoch" int4,
  "arch" varchar(16) COLLATE "pg_catalog"."default" NOT NULL,
  "external_repo_id" int4 NOT NULL,
  "payloadhash" text COLLATE "pg_catalog"."default" NOT NULL,
  "size" int8 NOT NULL,
  "buildtime" int8 NOT NULL,
  "metadata_only" bool NOT NULL DEFAULT false,
  "extra" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for rpmsigs
-- ----------------------------
DROP TABLE IF EXISTS "public"."rpmsigs";
CREATE TABLE "public"."rpmsigs" (
  "rpm_id" int4 NOT NULL,
  "sigkey" text COLLATE "pg_catalog"."default" NOT NULL,
  "sighash" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for sessions
-- ----------------------------
DROP TABLE IF EXISTS "public"."sessions";
CREATE TABLE "public"."sessions" (
  "id" int4 NOT NULL DEFAULT nextval('sessions_id_seq'::regclass),
  "user_id" int4 NOT NULL,
  "expired" bool NOT NULL DEFAULT false,
  "master" int4,
  "key" varchar(255) COLLATE "pg_catalog"."default",
  "authtype" int4,
  "hostip" varchar(255) COLLATE "pg_catalog"."default",
  "callnum" int4,
  "start_time" timestamptz(6) NOT NULL DEFAULT now(),
  "update_time" timestamptz(6) NOT NULL DEFAULT now(),
  "exclusive" bool
)
;

-- ----------------------------
-- Table structure for standard_buildroot
-- ----------------------------
DROP TABLE IF EXISTS "public"."standard_buildroot";
CREATE TABLE "public"."standard_buildroot" (
  "buildroot_id" int4 NOT NULL,
  "host_id" int4 NOT NULL,
  "repo_id" int4 NOT NULL,
  "task_id" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "retire_event" int4,
  "state" int4
)
;

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag";
CREATE TABLE "public"."tag" (
  "id" int4 NOT NULL DEFAULT nextval('tag_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for tag_config
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_config";
CREATE TABLE "public"."tag_config" (
  "tag_id" int4 NOT NULL,
  "arches" text COLLATE "pg_catalog"."default",
  "perm_id" int4,
  "locked" bool NOT NULL DEFAULT false,
  "maven_support" bool NOT NULL DEFAULT false,
  "maven_include_all" bool NOT NULL DEFAULT false,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for tag_external_repos
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_external_repos";
CREATE TABLE "public"."tag_external_repos" (
  "tag_id" int4 NOT NULL,
  "external_repo_id" int4 NOT NULL,
  "priority" int4 NOT NULL,
  "merge_mode" text COLLATE "pg_catalog"."default" NOT NULL DEFAULT 'koji'::text,
  "arches" text COLLATE "pg_catalog"."default",
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for tag_extra
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_extra";
CREATE TABLE "public"."tag_extra" (
  "tag_id" int4 NOT NULL,
  "key" text COLLATE "pg_catalog"."default" NOT NULL,
  "value" text COLLATE "pg_catalog"."default",
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for tag_inheritance
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_inheritance";
CREATE TABLE "public"."tag_inheritance" (
  "tag_id" int4 NOT NULL,
  "parent_id" int4 NOT NULL,
  "priority" int4 NOT NULL,
  "maxdepth" int4,
  "intransitive" bool NOT NULL DEFAULT false,
  "noconfig" bool NOT NULL DEFAULT false,
  "pkg_filter" text COLLATE "pg_catalog"."default",
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for tag_listing
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_listing";
CREATE TABLE "public"."tag_listing" (
  "build_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for tag_package_owners
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_package_owners";
CREATE TABLE "public"."tag_package_owners" (
  "package_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL,
  "owner" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for tag_packages
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_packages";
CREATE TABLE "public"."tag_packages" (
  "package_id" int4 NOT NULL,
  "tag_id" int4 NOT NULL,
  "blocked" bool NOT NULL DEFAULT false,
  "extra_arches" text COLLATE "pg_catalog"."default",
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for tag_updates
-- ----------------------------
DROP TABLE IF EXISTS "public"."tag_updates";
CREATE TABLE "public"."tag_updates" (
  "id" int4 NOT NULL DEFAULT nextval('tag_updates_id_seq'::regclass),
  "tag_id" int4 NOT NULL,
  "update_event" int4 NOT NULL DEFAULT get_event(),
  "updater_id" int4 NOT NULL,
  "update_type" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS "public"."task";
CREATE TABLE "public"."task" (
  "id" int4 NOT NULL DEFAULT nextval('task_id_seq'::regclass),
  "state" int4,
  "create_time" timestamptz(6) NOT NULL DEFAULT now(),
  "start_time" timestamptz(6),
  "completion_time" timestamptz(6),
  "channel_id" int4 NOT NULL,
  "host_id" int4,
  "parent" int4,
  "label" varchar(255) COLLATE "pg_catalog"."default",
  "waiting" bool,
  "awaited" bool,
  "owner" int4 NOT NULL,
  "method" text COLLATE "pg_catalog"."default",
  "request" text COLLATE "pg_catalog"."default",
  "result" text COLLATE "pg_catalog"."default",
  "eta" int4,
  "arch" varchar(16) COLLATE "pg_catalog"."default" NOT NULL,
  "priority" int4,
  "weight" float8 NOT NULL DEFAULT 1.0
)
;

-- ----------------------------
-- Table structure for user_groups
-- ----------------------------
DROP TABLE IF EXISTS "public"."user_groups";
CREATE TABLE "public"."user_groups" (
  "user_id" int4 NOT NULL,
  "group_id" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for user_krb_principals
-- ----------------------------
DROP TABLE IF EXISTS "public"."user_krb_principals";
CREATE TABLE "public"."user_krb_principals" (
  "user_id" int4 NOT NULL,
  "krb_principal" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for user_perms
-- ----------------------------
DROP TABLE IF EXISTS "public"."user_perms";
CREATE TABLE "public"."user_perms" (
  "user_id" int4 NOT NULL,
  "perm_id" int4 NOT NULL,
  "create_event" int4 NOT NULL DEFAULT get_event(),
  "revoke_event" int4,
  "creator_id" int4 NOT NULL,
  "revoker_id" int4,
  "active" bool DEFAULT true
)
;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS "public"."users";
CREATE TABLE "public"."users" (
  "id" int4 NOT NULL DEFAULT nextval('users_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "password" varchar(255) COLLATE "pg_catalog"."default",
  "status" int4 NOT NULL,
  "usertype" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for volume
-- ----------------------------
DROP TABLE IF EXISTS "public"."volume";
CREATE TABLE "public"."volume" (
  "id" int4 NOT NULL DEFAULT nextval('volume_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for win_archives
-- ----------------------------
DROP TABLE IF EXISTS "public"."win_archives";
CREATE TABLE "public"."win_archives" (
  "archive_id" int4 NOT NULL,
  "relpath" text COLLATE "pg_catalog"."default" NOT NULL,
  "platforms" text COLLATE "pg_catalog"."default" NOT NULL,
  "flags" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for win_builds
-- ----------------------------
DROP TABLE IF EXISTS "public"."win_builds";
CREATE TABLE "public"."win_builds" (
  "build_id" int4 NOT NULL,
  "platform" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Function structure for get_event
-- ----------------------------
DROP FUNCTION IF EXISTS "public"."get_event"();
CREATE OR REPLACE FUNCTION "public"."get_event"()
  RETURNS "pg_catalog"."int4" AS $BODY$
	INSERT INTO events (time) VALUES (clock_timestamp());
	SELECT currval('events_id_seq')::INTEGER;
$BODY$
  LANGUAGE sql VOLATILE
  COST 100;

-- ----------------------------
-- Function structure for get_event_time
-- ----------------------------
DROP FUNCTION IF EXISTS "public"."get_event_time"(int4);
CREATE OR REPLACE FUNCTION "public"."get_event_time"(int4)
  RETURNS "pg_catalog"."timestamptz" AS $BODY$
	SELECT time FROM events WHERE id=$1;
$BODY$
  LANGUAGE sql VOLATILE
  COST 100;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."archiveinfo_id_seq"
OWNED BY "public"."archiveinfo"."id";
SELECT setval('"public"."archiveinfo_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."archivetypes_id_seq"
OWNED BY "public"."archivetypes"."id";
SELECT setval('"public"."archivetypes_id_seq"', 68, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."btype_id_seq"
OWNED BY "public"."btype"."id";
SELECT setval('"public"."btype_id_seq"', 5, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."build_id_seq"
OWNED BY "public"."build"."id";
SELECT setval('"public"."build_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."build_notifications_block_id_seq"
OWNED BY "public"."build_notifications_block"."id";
SELECT setval('"public"."build_notifications_block_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."build_notifications_id_seq"
OWNED BY "public"."build_notifications"."id";
SELECT setval('"public"."build_notifications_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."build_target_id_seq"
OWNED BY "public"."build_target"."id";
SELECT setval('"public"."build_target_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."buildroot_id_seq"
OWNED BY "public"."buildroot"."id";
SELECT setval('"public"."buildroot_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."channels_id_seq"
OWNED BY "public"."channels"."id";
SELECT setval('"public"."channels_id_seq"', 9, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."content_generator_id_seq"
OWNED BY "public"."content_generator"."id";
SELECT setval('"public"."content_generator_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."events_id_seq"
OWNED BY "public"."events"."id";
SELECT setval('"public"."events_id_seq"', 7, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."external_repo_id_seq"
OWNED BY "public"."external_repo"."id";
SELECT setval('"public"."external_repo_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."groups_id_seq"
OWNED BY "public"."groups"."id";
SELECT setval('"public"."groups_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."host_id_seq"
OWNED BY "public"."host"."id";
SELECT setval('"public"."host_id_seq"', 6, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."package_id_seq"
OWNED BY "public"."package"."id";
SELECT setval('"public"."package_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."permissions_id_seq"
OWNED BY "public"."permissions"."id";
SELECT setval('"public"."permissions_id_seq"', 15, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."proton_queue_id_seq"
OWNED BY "public"."proton_queue"."id";
SELECT setval('"public"."proton_queue_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."repo_id_seq"
OWNED BY "public"."repo"."id";
SELECT setval('"public"."repo_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."rpminfo_id_seq"
OWNED BY "public"."rpminfo"."id";
SELECT setval('"public"."rpminfo_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."sessions_id_seq"
OWNED BY "public"."sessions"."id";
SELECT setval('"public"."sessions_id_seq"', 12, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tag_id_seq"
OWNED BY "public"."tag"."id";
SELECT setval('"public"."tag_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tag_updates_id_seq"
OWNED BY "public"."tag_updates"."id";
SELECT setval('"public"."tag_updates_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."task_id_seq"
OWNED BY "public"."task"."id";
SELECT setval('"public"."task_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."users_id_seq"
OWNED BY "public"."users"."id";
SELECT setval('"public"."users_id_seq"', 7, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."volume_id_seq"
OWNED BY "public"."volume"."id";
SELECT setval('"public"."volume_id_seq"', 2, false);

-- ----------------------------
-- Indexes structure for table archive_components
-- ----------------------------
CREATE INDEX "archive_components_idx" ON "public"."archive_components" USING btree (
  "component_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table archive_components
-- ----------------------------
ALTER TABLE "public"."archive_components" ADD CONSTRAINT "archive_components_archive_id_component_id_key" UNIQUE ("archive_id", "component_id");

-- ----------------------------
-- Indexes structure for table archive_rpm_components
-- ----------------------------
CREATE INDEX "rpm_components_idx" ON "public"."archive_rpm_components" USING btree (
  "rpm_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table archive_rpm_components
-- ----------------------------
ALTER TABLE "public"."archive_rpm_components" ADD CONSTRAINT "archive_rpm_components_archive_id_rpm_id_key" UNIQUE ("archive_id", "rpm_id");

-- ----------------------------
-- Indexes structure for table archiveinfo
-- ----------------------------
CREATE INDEX "archiveinfo_build_idx" ON "public"."archiveinfo" USING btree (
  "build_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "archiveinfo_buildroot_idx" ON "public"."archiveinfo" USING btree (
  "buildroot_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "archiveinfo_filename_idx" ON "public"."archiveinfo" USING btree (
  "filename" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "archiveinfo_type_idx" ON "public"."archiveinfo" USING btree (
  "type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table archiveinfo
-- ----------------------------
ALTER TABLE "public"."archiveinfo" ADD CONSTRAINT "archiveinfo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table archivetypes
-- ----------------------------
ALTER TABLE "public"."archivetypes" ADD CONSTRAINT "archivetypes_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table archivetypes
-- ----------------------------
ALTER TABLE "public"."archivetypes" ADD CONSTRAINT "archivetypes_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table btype
-- ----------------------------
ALTER TABLE "public"."btype" ADD CONSTRAINT "btype_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table btype
-- ----------------------------
ALTER TABLE "public"."btype" ADD CONSTRAINT "btype_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table build
-- ----------------------------
CREATE INDEX "build_by_pkg_id" ON "public"."build" USING btree (
  "pkg_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "build_completion" ON "public"."build" USING btree (
  "completion_time" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table build
-- ----------------------------
ALTER TABLE "public"."build" ADD CONSTRAINT "build_pkg_ver_rel" UNIQUE ("pkg_id", "version", "release");

-- ----------------------------
-- Checks structure for table build
-- ----------------------------
ALTER TABLE "public"."build" ADD CONSTRAINT "completion_sane" CHECK ((((state = 0) AND (completion_time IS NULL)) OR ((state <> 0) AND (completion_time IS NOT NULL))));

-- ----------------------------
-- Primary Key structure for table build
-- ----------------------------
ALTER TABLE "public"."build" ADD CONSTRAINT "build_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table build_notifications
-- ----------------------------
ALTER TABLE "public"."build_notifications" ADD CONSTRAINT "build_notifications_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table build_notifications_block
-- ----------------------------
ALTER TABLE "public"."build_notifications_block" ADD CONSTRAINT "build_notifications_block_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table build_reservations
-- ----------------------------
CREATE INDEX "build_reservations_created" ON "public"."build_reservations" USING btree (
  "created" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table build_reservations
-- ----------------------------
ALTER TABLE "public"."build_reservations" ADD CONSTRAINT "build_reservations_pkey" PRIMARY KEY ("build_id");

-- ----------------------------
-- Uniques structure for table build_target
-- ----------------------------
ALTER TABLE "public"."build_target" ADD CONSTRAINT "build_target_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table build_target
-- ----------------------------
ALTER TABLE "public"."build_target" ADD CONSTRAINT "build_target_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table build_target_config
-- ----------------------------
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_build_target_id_active_key" UNIQUE ("build_target_id", "active");

-- ----------------------------
-- Checks structure for table build_target_config
-- ----------------------------
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table build_target_config
-- ----------------------------
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_pkey" PRIMARY KEY ("create_event", "build_target_id");

-- ----------------------------
-- Primary Key structure for table build_types
-- ----------------------------
ALTER TABLE "public"."build_types" ADD CONSTRAINT "build_types_pkey" PRIMARY KEY ("build_id", "btype_id");

-- ----------------------------
-- Checks structure for table buildroot
-- ----------------------------
ALTER TABLE "public"."buildroot" ADD CONSTRAINT "container_sane" CHECK ((((container_type IS NULL) AND (container_arch IS NULL)) OR ((container_type IS NOT NULL) AND (container_arch IS NOT NULL))));
ALTER TABLE "public"."buildroot" ADD CONSTRAINT "cg_sane" CHECK ((((cg_id IS NULL) AND (cg_version IS NULL)) OR ((cg_id IS NOT NULL) AND (cg_version IS NOT NULL))));

-- ----------------------------
-- Primary Key structure for table buildroot
-- ----------------------------
ALTER TABLE "public"."buildroot" ADD CONSTRAINT "buildroot_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table buildroot_archives
-- ----------------------------
CREATE INDEX "buildroot_archives_archive_idx" ON "public"."buildroot_archives" USING btree (
  "archive_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table buildroot_archives
-- ----------------------------
ALTER TABLE "public"."buildroot_archives" ADD CONSTRAINT "buildroot_archives_pkey" PRIMARY KEY ("buildroot_id", "archive_id");

-- ----------------------------
-- Indexes structure for table buildroot_listing
-- ----------------------------
CREATE INDEX "buildroot_listing_rpms" ON "public"."buildroot_listing" USING btree (
  "rpm_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table buildroot_listing
-- ----------------------------
ALTER TABLE "public"."buildroot_listing" ADD CONSTRAINT "buildroot_listing_buildroot_id_rpm_id_key" UNIQUE ("buildroot_id", "rpm_id");

-- ----------------------------
-- Primary Key structure for table buildroot_tools_info
-- ----------------------------
ALTER TABLE "public"."buildroot_tools_info" ADD CONSTRAINT "buildroot_tools_info_pkey" PRIMARY KEY ("buildroot_id", "tool");

-- ----------------------------
-- Uniques structure for table cg_users
-- ----------------------------
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_cg_id_user_id_active_key" UNIQUE ("cg_id", "user_id", "active");

-- ----------------------------
-- Checks structure for table cg_users
-- ----------------------------
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table cg_users
-- ----------------------------
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_pkey" PRIMARY KEY ("create_event", "cg_id", "user_id");

-- ----------------------------
-- Uniques structure for table channels
-- ----------------------------
ALTER TABLE "public"."channels" ADD CONSTRAINT "channels_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table channels
-- ----------------------------
ALTER TABLE "public"."channels" ADD CONSTRAINT "channels_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table content_generator
-- ----------------------------
ALTER TABLE "public"."content_generator" ADD CONSTRAINT "content_generator_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table content_generator
-- ----------------------------
ALTER TABLE "public"."content_generator" ADD CONSTRAINT "content_generator_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table event_labels
-- ----------------------------
ALTER TABLE "public"."event_labels" ADD CONSTRAINT "event_labels_label_key" UNIQUE ("label");

-- ----------------------------
-- Primary Key structure for table events
-- ----------------------------
ALTER TABLE "public"."events" ADD CONSTRAINT "events_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table external_repo
-- ----------------------------
ALTER TABLE "public"."external_repo" ADD CONSTRAINT "external_repo_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table external_repo
-- ----------------------------
ALTER TABLE "public"."external_repo" ADD CONSTRAINT "external_repo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table external_repo_config
-- ----------------------------
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_external_repo_id_active_key" UNIQUE ("external_repo_id", "active");

-- ----------------------------
-- Checks structure for table external_repo_config
-- ----------------------------
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table external_repo_config
-- ----------------------------
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_pkey" PRIMARY KEY ("create_event", "external_repo_id");

-- ----------------------------
-- Uniques structure for table group_config
-- ----------------------------
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_group_id_tag_id_active_key" UNIQUE ("group_id", "tag_id", "active");

-- ----------------------------
-- Checks structure for table group_config
-- ----------------------------
ALTER TABLE "public"."group_config" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table group_config
-- ----------------------------
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_pkey" PRIMARY KEY ("create_event", "group_id", "tag_id");

-- ----------------------------
-- Uniques structure for table group_package_listing
-- ----------------------------
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_group_id_tag_id_package_active_key" UNIQUE ("group_id", "tag_id", "package", "active");

-- ----------------------------
-- Checks structure for table group_package_listing
-- ----------------------------
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table group_package_listing
-- ----------------------------
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_pkey" PRIMARY KEY ("create_event", "group_id", "tag_id", "package");

-- ----------------------------
-- Uniques structure for table group_req_listing
-- ----------------------------
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_group_id_tag_id_req_id_active_key" UNIQUE ("group_id", "tag_id", "req_id", "active");

-- ----------------------------
-- Checks structure for table group_req_listing
-- ----------------------------
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table group_req_listing
-- ----------------------------
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_pkey" PRIMARY KEY ("create_event", "group_id", "tag_id", "req_id");

-- ----------------------------
-- Uniques structure for table groups
-- ----------------------------
ALTER TABLE "public"."groups" ADD CONSTRAINT "groups_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table groups
-- ----------------------------
ALTER TABLE "public"."groups" ADD CONSTRAINT "groups_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table host
-- ----------------------------
ALTER TABLE "public"."host" ADD CONSTRAINT "host_name_key" UNIQUE ("name");

-- ----------------------------
-- Checks structure for table host
-- ----------------------------
ALTER TABLE "public"."host" ADD CONSTRAINT "host_task_load_check" CHECK ((NOT (task_load < (0)::double precision)));

-- ----------------------------
-- Primary Key structure for table host
-- ----------------------------
ALTER TABLE "public"."host" ADD CONSTRAINT "host_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table host_channels
-- ----------------------------
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_host_id_channel_id_active_key" UNIQUE ("host_id", "channel_id", "active");

-- ----------------------------
-- Checks structure for table host_channels
-- ----------------------------
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table host_channels
-- ----------------------------
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_pkey" PRIMARY KEY ("create_event", "host_id", "channel_id");

-- ----------------------------
-- Indexes structure for table host_config
-- ----------------------------
CREATE INDEX "host_config_by_active_and_enabled" ON "public"."host_config" USING btree (
  "active" "pg_catalog"."bool_ops" ASC NULLS LAST,
  "enabled" "pg_catalog"."bool_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table host_config
-- ----------------------------
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_host_id_active_key" UNIQUE ("host_id", "active");

-- ----------------------------
-- Checks structure for table host_config
-- ----------------------------
ALTER TABLE "public"."host_config" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_active_check" CHECK (active);
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_capacity_check" CHECK ((capacity > (1)::double precision));

-- ----------------------------
-- Primary Key structure for table host_config
-- ----------------------------
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_pkey" PRIMARY KEY ("create_event", "host_id");

-- ----------------------------
-- Primary Key structure for table image_archives
-- ----------------------------
ALTER TABLE "public"."image_archives" ADD CONSTRAINT "image_archives_pkey" PRIMARY KEY ("archive_id");

-- ----------------------------
-- Primary Key structure for table image_builds
-- ----------------------------
ALTER TABLE "public"."image_builds" ADD CONSTRAINT "image_builds_pkey" PRIMARY KEY ("build_id");

-- ----------------------------
-- Primary Key structure for table maven_archives
-- ----------------------------
ALTER TABLE "public"."maven_archives" ADD CONSTRAINT "maven_archives_pkey" PRIMARY KEY ("archive_id");

-- ----------------------------
-- Primary Key structure for table maven_builds
-- ----------------------------
ALTER TABLE "public"."maven_builds" ADD CONSTRAINT "maven_builds_pkey" PRIMARY KEY ("build_id");

-- ----------------------------
-- Uniques structure for table package
-- ----------------------------
ALTER TABLE "public"."package" ADD CONSTRAINT "package_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table package
-- ----------------------------
ALTER TABLE "public"."package" ADD CONSTRAINT "package_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table permissions
-- ----------------------------
ALTER TABLE "public"."permissions" ADD CONSTRAINT "permissions_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table permissions
-- ----------------------------
ALTER TABLE "public"."permissions" ADD CONSTRAINT "permissions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table proton_queue
-- ----------------------------
ALTER TABLE "public"."proton_queue" ADD CONSTRAINT "proton_queue_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table repo
-- ----------------------------
ALTER TABLE "public"."repo" ADD CONSTRAINT "repo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table rpminfo
-- ----------------------------
CREATE INDEX "rpminfo_build" ON "public"."rpminfo" USING btree (
  "build_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table rpminfo
-- ----------------------------
ALTER TABLE "public"."rpminfo" ADD CONSTRAINT "rpminfo_unique_nvra" UNIQUE ("name", "version", "release", "arch", "external_repo_id");

-- ----------------------------
-- Primary Key structure for table rpminfo
-- ----------------------------
ALTER TABLE "public"."rpminfo" ADD CONSTRAINT "rpminfo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table rpmsigs
-- ----------------------------
ALTER TABLE "public"."rpmsigs" ADD CONSTRAINT "rpmsigs_no_resign" UNIQUE ("rpm_id", "sigkey");

-- ----------------------------
-- Indexes structure for table sessions
-- ----------------------------
CREATE INDEX "sessions_active_and_recent" ON "public"."sessions" USING btree (
  "expired" "pg_catalog"."bool_ops" ASC NULLS LAST,
  "master" "pg_catalog"."int4_ops" ASC NULLS LAST,
  "update_time" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
) WHERE expired = false AND master IS NULL;
CREATE INDEX "sessions_expired" ON "public"."sessions" USING btree (
  "expired" "pg_catalog"."bool_ops" ASC NULLS LAST
);
CREATE INDEX "sessions_master" ON "public"."sessions" USING btree (
  "master" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table sessions
-- ----------------------------
ALTER TABLE "public"."sessions" ADD CONSTRAINT "sessions_user_id_exclusive_key" UNIQUE ("user_id", "exclusive");

-- ----------------------------
-- Checks structure for table sessions
-- ----------------------------
ALTER TABLE "public"."sessions" ADD CONSTRAINT "exclusive_expired_sane" CHECK (((expired IS FALSE) OR (exclusive IS NULL)));
ALTER TABLE "public"."sessions" ADD CONSTRAINT "no_exclusive_subsessions" CHECK (((master IS NULL) OR (exclusive IS NULL)));
ALTER TABLE "public"."sessions" ADD CONSTRAINT "sessions_exclusive_check" CHECK (exclusive);

-- ----------------------------
-- Primary Key structure for table sessions
-- ----------------------------
ALTER TABLE "public"."sessions" ADD CONSTRAINT "sessions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table standard_buildroot
-- ----------------------------
ALTER TABLE "public"."standard_buildroot" ADD CONSTRAINT "standard_buildroot_pkey" PRIMARY KEY ("buildroot_id");

-- ----------------------------
-- Uniques structure for table tag
-- ----------------------------
ALTER TABLE "public"."tag" ADD CONSTRAINT "tag_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table tag
-- ----------------------------
ALTER TABLE "public"."tag" ADD CONSTRAINT "tag_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table tag_config
-- ----------------------------
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_tag_id_active_key" UNIQUE ("tag_id", "active");

-- ----------------------------
-- Checks structure for table tag_config
-- ----------------------------
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table tag_config
-- ----------------------------
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_pkey" PRIMARY KEY ("create_event", "tag_id");

-- ----------------------------
-- Uniques structure for table tag_external_repos
-- ----------------------------
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_tag_id_priority_active_key" UNIQUE ("tag_id", "priority", "active");
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_tag_id_external_repo_id_active_key" UNIQUE ("tag_id", "external_repo_id", "active");

-- ----------------------------
-- Checks structure for table tag_external_repos
-- ----------------------------
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table tag_external_repos
-- ----------------------------
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_pkey" PRIMARY KEY ("create_event", "tag_id", "priority");

-- ----------------------------
-- Uniques structure for table tag_extra
-- ----------------------------
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_tag_id_key_active_key" UNIQUE ("tag_id", "key", "active");

-- ----------------------------
-- Checks structure for table tag_extra
-- ----------------------------
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table tag_extra
-- ----------------------------
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_pkey" PRIMARY KEY ("create_event", "tag_id", "key");

-- ----------------------------
-- Indexes structure for table tag_inheritance
-- ----------------------------
CREATE INDEX "tag_inheritance_by_parent" ON "public"."tag_inheritance" USING btree (
  "parent_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table tag_inheritance
-- ----------------------------
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_tag_id_priority_active_key" UNIQUE ("tag_id", "priority", "active");
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_tag_id_parent_id_active_key" UNIQUE ("tag_id", "parent_id", "active");

-- ----------------------------
-- Checks structure for table tag_inheritance
-- ----------------------------
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table tag_inheritance
-- ----------------------------
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_pkey" PRIMARY KEY ("create_event", "tag_id", "priority");

-- ----------------------------
-- Indexes structure for table tag_listing
-- ----------------------------
CREATE INDEX "tag_listing_tag_id_key" ON "public"."tag_listing" USING btree (
  "tag_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table tag_listing
-- ----------------------------
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_build_id_tag_id_active_key" UNIQUE ("build_id", "tag_id", "active");

-- ----------------------------
-- Checks structure for table tag_listing
-- ----------------------------
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table tag_listing
-- ----------------------------
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_pkey" PRIMARY KEY ("create_event", "build_id", "tag_id");

-- ----------------------------
-- Uniques structure for table tag_package_owners
-- ----------------------------
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_package_id_tag_id_active_key" UNIQUE ("package_id", "tag_id", "active");

-- ----------------------------
-- Checks structure for table tag_package_owners
-- ----------------------------
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table tag_package_owners
-- ----------------------------
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_pkey" PRIMARY KEY ("create_event", "package_id", "tag_id");

-- ----------------------------
-- Indexes structure for table tag_packages
-- ----------------------------
CREATE INDEX "tag_packages_active_tag_id" ON "public"."tag_packages" USING btree (
  "active" "pg_catalog"."bool_ops" ASC NULLS LAST,
  "tag_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "tag_packages_create_event" ON "public"."tag_packages" USING btree (
  "create_event" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "tag_packages_revoke_event" ON "public"."tag_packages" USING btree (
  "revoke_event" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table tag_packages
-- ----------------------------
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_package_id_tag_id_active_key" UNIQUE ("package_id", "tag_id", "active");

-- ----------------------------
-- Checks structure for table tag_packages
-- ----------------------------
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table tag_packages
-- ----------------------------
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_pkey" PRIMARY KEY ("create_event", "package_id", "tag_id");

-- ----------------------------
-- Indexes structure for table tag_updates
-- ----------------------------
CREATE INDEX "tag_updates_by_event" ON "public"."tag_updates" USING btree (
  "update_event" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "tag_updates_by_tag" ON "public"."tag_updates" USING btree (
  "tag_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table tag_updates
-- ----------------------------
ALTER TABLE "public"."tag_updates" ADD CONSTRAINT "tag_updates_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table task
-- ----------------------------
CREATE INDEX "task_by_host" ON "public"."task" USING btree (
  "host_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "task_by_no_parent_state_method" ON "public"."task" USING btree (
  "parent" "pg_catalog"."int4_ops" ASC NULLS LAST,
  "state" "pg_catalog"."int4_ops" ASC NULLS LAST,
  "method" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
) WHERE parent IS NULL;
CREATE INDEX "task_by_state" ON "public"."task" USING btree (
  "state" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table task
-- ----------------------------
ALTER TABLE "public"."task" ADD CONSTRAINT "task_parent_label_key" UNIQUE ("parent", "label");

-- ----------------------------
-- Checks structure for table task
-- ----------------------------
ALTER TABLE "public"."task" ADD CONSTRAINT "parent_label_sane" CHECK (((parent IS NOT NULL) OR (label IS NULL)));
ALTER TABLE "public"."task" ADD CONSTRAINT "task_weight_check" CHECK ((NOT (weight < (0)::double precision)));

-- ----------------------------
-- Primary Key structure for table task
-- ----------------------------
ALTER TABLE "public"."task" ADD CONSTRAINT "task_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table user_groups
-- ----------------------------
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_user_id_group_id_active_key" UNIQUE ("user_id", "group_id", "active");

-- ----------------------------
-- Checks structure for table user_groups
-- ----------------------------
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table user_groups
-- ----------------------------
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_pkey" PRIMARY KEY ("create_event", "user_id", "group_id");

-- ----------------------------
-- Uniques structure for table user_krb_principals
-- ----------------------------
ALTER TABLE "public"."user_krb_principals" ADD CONSTRAINT "user_krb_principals_krb_principal_key" UNIQUE ("krb_principal");

-- ----------------------------
-- Primary Key structure for table user_krb_principals
-- ----------------------------
ALTER TABLE "public"."user_krb_principals" ADD CONSTRAINT "user_krb_principals_pkey" PRIMARY KEY ("user_id", "krb_principal");

-- ----------------------------
-- Uniques structure for table user_perms
-- ----------------------------
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_user_id_perm_id_active_key" UNIQUE ("user_id", "perm_id", "active");

-- ----------------------------
-- Checks structure for table user_perms
-- ----------------------------
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "active_revoke_sane" CHECK ((((active IS NULL) AND (revoke_event IS NOT NULL) AND (revoker_id IS NOT NULL)) OR ((active IS NOT NULL) AND (revoke_event IS NULL) AND (revoker_id IS NULL))));
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_active_check" CHECK (active);

-- ----------------------------
-- Primary Key structure for table user_perms
-- ----------------------------
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_pkey" PRIMARY KEY ("create_event", "user_id", "perm_id");

-- ----------------------------
-- Uniques structure for table users
-- ----------------------------
ALTER TABLE "public"."users" ADD CONSTRAINT "users_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table users
-- ----------------------------
ALTER TABLE "public"."users" ADD CONSTRAINT "users_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table volume
-- ----------------------------
ALTER TABLE "public"."volume" ADD CONSTRAINT "volume_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table volume
-- ----------------------------
ALTER TABLE "public"."volume" ADD CONSTRAINT "volume_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table win_archives
-- ----------------------------
ALTER TABLE "public"."win_archives" ADD CONSTRAINT "win_archives_pkey" PRIMARY KEY ("archive_id");

-- ----------------------------
-- Primary Key structure for table win_builds
-- ----------------------------
ALTER TABLE "public"."win_builds" ADD CONSTRAINT "win_builds_pkey" PRIMARY KEY ("build_id");

-- ----------------------------
-- Foreign Keys structure for table archive_components
-- ----------------------------
ALTER TABLE "public"."archive_components" ADD CONSTRAINT "archive_components_archive_id_fkey" FOREIGN KEY ("archive_id") REFERENCES "public"."archiveinfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."archive_components" ADD CONSTRAINT "archive_components_component_id_fkey" FOREIGN KEY ("component_id") REFERENCES "public"."archiveinfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table archive_rpm_components
-- ----------------------------
ALTER TABLE "public"."archive_rpm_components" ADD CONSTRAINT "archive_rpm_components_archive_id_fkey" FOREIGN KEY ("archive_id") REFERENCES "public"."archiveinfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."archive_rpm_components" ADD CONSTRAINT "archive_rpm_components_rpm_id_fkey" FOREIGN KEY ("rpm_id") REFERENCES "public"."rpminfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table archiveinfo
-- ----------------------------
ALTER TABLE "public"."archiveinfo" ADD CONSTRAINT "archiveinfo_btype_id_fkey" FOREIGN KEY ("btype_id") REFERENCES "public"."btype" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."archiveinfo" ADD CONSTRAINT "archiveinfo_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."archiveinfo" ADD CONSTRAINT "archiveinfo_buildroot_id_fkey" FOREIGN KEY ("buildroot_id") REFERENCES "public"."buildroot" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."archiveinfo" ADD CONSTRAINT "archiveinfo_type_id_fkey" FOREIGN KEY ("type_id") REFERENCES "public"."archivetypes" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table build
-- ----------------------------
ALTER TABLE "public"."build" ADD CONSTRAINT "build_cg_id_fkey" FOREIGN KEY ("cg_id") REFERENCES "public"."content_generator" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build" ADD CONSTRAINT "build_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build" ADD CONSTRAINT "build_owner_fkey" FOREIGN KEY ("owner") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build" ADD CONSTRAINT "build_pkg_id_fkey" FOREIGN KEY ("pkg_id") REFERENCES "public"."package" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE;
ALTER TABLE "public"."build" ADD CONSTRAINT "build_task_id_fkey" FOREIGN KEY ("task_id") REFERENCES "public"."task" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build" ADD CONSTRAINT "build_volume_id_fkey" FOREIGN KEY ("volume_id") REFERENCES "public"."volume" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table build_notifications
-- ----------------------------
ALTER TABLE "public"."build_notifications" ADD CONSTRAINT "build_notifications_package_id_fkey" FOREIGN KEY ("package_id") REFERENCES "public"."package" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_notifications" ADD CONSTRAINT "build_notifications_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_notifications" ADD CONSTRAINT "build_notifications_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table build_notifications_block
-- ----------------------------
ALTER TABLE "public"."build_notifications_block" ADD CONSTRAINT "build_notifications_block_package_id_fkey" FOREIGN KEY ("package_id") REFERENCES "public"."package" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_notifications_block" ADD CONSTRAINT "build_notifications_block_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_notifications_block" ADD CONSTRAINT "build_notifications_block_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table build_reservations
-- ----------------------------
ALTER TABLE "public"."build_reservations" ADD CONSTRAINT "build_reservations_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table build_target_config
-- ----------------------------
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_build_tag_fkey" FOREIGN KEY ("build_tag") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_build_target_id_fkey" FOREIGN KEY ("build_target_id") REFERENCES "public"."build_target" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_dest_tag_fkey" FOREIGN KEY ("dest_tag") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_target_config" ADD CONSTRAINT "build_target_config_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table build_types
-- ----------------------------
ALTER TABLE "public"."build_types" ADD CONSTRAINT "build_types_btype_id_fkey" FOREIGN KEY ("btype_id") REFERENCES "public"."btype" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."build_types" ADD CONSTRAINT "build_types_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table buildroot
-- ----------------------------
ALTER TABLE "public"."buildroot" ADD CONSTRAINT "buildroot_cg_id_fkey" FOREIGN KEY ("cg_id") REFERENCES "public"."content_generator" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table buildroot_archives
-- ----------------------------
ALTER TABLE "public"."buildroot_archives" ADD CONSTRAINT "buildroot_archives_archive_id_fkey" FOREIGN KEY ("archive_id") REFERENCES "public"."archiveinfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."buildroot_archives" ADD CONSTRAINT "buildroot_archives_buildroot_id_fkey" FOREIGN KEY ("buildroot_id") REFERENCES "public"."buildroot" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table buildroot_listing
-- ----------------------------
ALTER TABLE "public"."buildroot_listing" ADD CONSTRAINT "buildroot_listing_buildroot_id_fkey" FOREIGN KEY ("buildroot_id") REFERENCES "public"."buildroot" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."buildroot_listing" ADD CONSTRAINT "buildroot_listing_rpm_id_fkey" FOREIGN KEY ("rpm_id") REFERENCES "public"."rpminfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table buildroot_tools_info
-- ----------------------------
ALTER TABLE "public"."buildroot_tools_info" ADD CONSTRAINT "buildroot_tools_info_buildroot_id_fkey" FOREIGN KEY ("buildroot_id") REFERENCES "public"."buildroot" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table cg_users
-- ----------------------------
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_cg_id_fkey" FOREIGN KEY ("cg_id") REFERENCES "public"."content_generator" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."cg_users" ADD CONSTRAINT "cg_users_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table event_labels
-- ----------------------------
ALTER TABLE "public"."event_labels" ADD CONSTRAINT "event_labels_event_id_fkey" FOREIGN KEY ("event_id") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table external_repo_config
-- ----------------------------
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_external_repo_id_fkey" FOREIGN KEY ("external_repo_id") REFERENCES "public"."external_repo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."external_repo_config" ADD CONSTRAINT "external_repo_config_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table group_config
-- ----------------------------
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_group_id_fkey" FOREIGN KEY ("group_id") REFERENCES "public"."groups" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_config" ADD CONSTRAINT "group_config_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table group_package_listing
-- ----------------------------
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_group_id_fkey" FOREIGN KEY ("group_id") REFERENCES "public"."groups" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_package_listing" ADD CONSTRAINT "group_package_listing_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table group_req_listing
-- ----------------------------
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_group_id_fkey" FOREIGN KEY ("group_id") REFERENCES "public"."groups" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_req_id_fkey" FOREIGN KEY ("req_id") REFERENCES "public"."groups" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."group_req_listing" ADD CONSTRAINT "group_req_listing_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table host
-- ----------------------------
ALTER TABLE "public"."host" ADD CONSTRAINT "host_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table host_channels
-- ----------------------------
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_channel_id_fkey" FOREIGN KEY ("channel_id") REFERENCES "public"."channels" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_host_id_fkey" FOREIGN KEY ("host_id") REFERENCES "public"."host" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_channels" ADD CONSTRAINT "host_channels_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table host_config
-- ----------------------------
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_host_id_fkey" FOREIGN KEY ("host_id") REFERENCES "public"."host" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."host_config" ADD CONSTRAINT "host_config_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table image_archives
-- ----------------------------
ALTER TABLE "public"."image_archives" ADD CONSTRAINT "image_archives_archive_id_fkey" FOREIGN KEY ("archive_id") REFERENCES "public"."archiveinfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table image_builds
-- ----------------------------
ALTER TABLE "public"."image_builds" ADD CONSTRAINT "image_builds_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table maven_archives
-- ----------------------------
ALTER TABLE "public"."maven_archives" ADD CONSTRAINT "maven_archives_archive_id_fkey" FOREIGN KEY ("archive_id") REFERENCES "public"."archiveinfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table maven_builds
-- ----------------------------
ALTER TABLE "public"."maven_builds" ADD CONSTRAINT "maven_builds_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table repo
-- ----------------------------
ALTER TABLE "public"."repo" ADD CONSTRAINT "repo_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."repo" ADD CONSTRAINT "repo_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."repo" ADD CONSTRAINT "repo_task_id_fkey" FOREIGN KEY ("task_id") REFERENCES "public"."task" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table rpminfo
-- ----------------------------
ALTER TABLE "public"."rpminfo" ADD CONSTRAINT "rpminfo_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rpminfo" ADD CONSTRAINT "rpminfo_buildroot_id_fkey" FOREIGN KEY ("buildroot_id") REFERENCES "public"."buildroot" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."rpminfo" ADD CONSTRAINT "rpminfo_external_repo_id_fkey" FOREIGN KEY ("external_repo_id") REFERENCES "public"."external_repo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table rpmsigs
-- ----------------------------
ALTER TABLE "public"."rpmsigs" ADD CONSTRAINT "rpmsigs_rpm_id_fkey" FOREIGN KEY ("rpm_id") REFERENCES "public"."rpminfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table sessions
-- ----------------------------
ALTER TABLE "public"."sessions" ADD CONSTRAINT "sessions_master_fkey" FOREIGN KEY ("master") REFERENCES "public"."sessions" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."sessions" ADD CONSTRAINT "sessions_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table standard_buildroot
-- ----------------------------
ALTER TABLE "public"."standard_buildroot" ADD CONSTRAINT "standard_buildroot_buildroot_id_fkey" FOREIGN KEY ("buildroot_id") REFERENCES "public"."buildroot" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."standard_buildroot" ADD CONSTRAINT "standard_buildroot_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."standard_buildroot" ADD CONSTRAINT "standard_buildroot_host_id_fkey" FOREIGN KEY ("host_id") REFERENCES "public"."host" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."standard_buildroot" ADD CONSTRAINT "standard_buildroot_repo_id_fkey" FOREIGN KEY ("repo_id") REFERENCES "public"."repo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."standard_buildroot" ADD CONSTRAINT "standard_buildroot_task_id_fkey" FOREIGN KEY ("task_id") REFERENCES "public"."task" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_config
-- ----------------------------
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_perm_id_fkey" FOREIGN KEY ("perm_id") REFERENCES "public"."permissions" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_config" ADD CONSTRAINT "tag_config_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_external_repos
-- ----------------------------
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_external_repo_id_fkey" FOREIGN KEY ("external_repo_id") REFERENCES "public"."external_repo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_external_repos" ADD CONSTRAINT "tag_external_repos_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_extra
-- ----------------------------
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_extra" ADD CONSTRAINT "tag_extra_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_inheritance
-- ----------------------------
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_parent_id_fkey" FOREIGN KEY ("parent_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_inheritance" ADD CONSTRAINT "tag_inheritance_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_listing
-- ----------------------------
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_listing" ADD CONSTRAINT "tag_listing_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_package_owners
-- ----------------------------
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_owner_fkey" FOREIGN KEY ("owner") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_package_id_fkey" FOREIGN KEY ("package_id") REFERENCES "public"."package" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_package_owners" ADD CONSTRAINT "tag_package_owners_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_packages
-- ----------------------------
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_package_id_fkey" FOREIGN KEY ("package_id") REFERENCES "public"."package" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_packages" ADD CONSTRAINT "tag_packages_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tag_updates
-- ----------------------------
ALTER TABLE "public"."tag_updates" ADD CONSTRAINT "tag_updates_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_updates" ADD CONSTRAINT "tag_updates_update_event_fkey" FOREIGN KEY ("update_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tag_updates" ADD CONSTRAINT "tag_updates_updater_id_fkey" FOREIGN KEY ("updater_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table task
-- ----------------------------
ALTER TABLE "public"."task" ADD CONSTRAINT "task_channel_id_fkey" FOREIGN KEY ("channel_id") REFERENCES "public"."channels" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."task" ADD CONSTRAINT "task_host_id_fkey" FOREIGN KEY ("host_id") REFERENCES "public"."host" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."task" ADD CONSTRAINT "task_owner_fkey" FOREIGN KEY ("owner") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."task" ADD CONSTRAINT "task_parent_fkey" FOREIGN KEY ("parent") REFERENCES "public"."task" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table user_groups
-- ----------------------------
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_group_id_fkey" FOREIGN KEY ("group_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_groups" ADD CONSTRAINT "user_groups_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table user_krb_principals
-- ----------------------------
ALTER TABLE "public"."user_krb_principals" ADD CONSTRAINT "user_krb_principals_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table user_perms
-- ----------------------------
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_create_event_fkey" FOREIGN KEY ("create_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_perm_id_fkey" FOREIGN KEY ("perm_id") REFERENCES "public"."permissions" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_revoke_event_fkey" FOREIGN KEY ("revoke_event") REFERENCES "public"."events" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_revoker_id_fkey" FOREIGN KEY ("revoker_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."user_perms" ADD CONSTRAINT "user_perms_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table win_archives
-- ----------------------------
ALTER TABLE "public"."win_archives" ADD CONSTRAINT "win_archives_archive_id_fkey" FOREIGN KEY ("archive_id") REFERENCES "public"."archiveinfo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table win_builds
-- ----------------------------
ALTER TABLE "public"."win_builds" ADD CONSTRAINT "win_builds_build_id_fkey" FOREIGN KEY ("build_id") REFERENCES "public"."build" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

```












---
