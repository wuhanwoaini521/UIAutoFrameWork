-- 测试数据
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "autotest";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "autotest2";

-- 测试环境需要删除的数据
--  方法
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "sigleGolbal";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "globalConstituent";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "gConstituentSystem";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "gConsSystemPda";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "singleSubsection";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "sConstituent";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "sConstituentSystem";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "sConsSystemPda";

DELETE FROM `cims_db`.`classic_spectrum_library` WHERE `libName` = "autoTest测试";
DELETE FROM `cims_db`.`methods` WHERE `methodName` = "autoreport";

-- 新建光谱库
INSERT INTO `cims_db`.`classic_spectrum_library`(`libName`, `libComments`, `libcreatedBy`) VALUES ('autoTest测试', '1', 'wuhan');

-- 新建报告方法
INSERT INTO `cims_db`.`methods`(`id`, `PiId`, `projectId`, `version`, `creater`, `methodName`, `methodType`, `paramDetail`, `isEdit`, `state`, `isCurve`, `createTime`, `isDel`, `isHandle`) VALUES (62812, 317, 1304, 1, 'wuhan', 'autoreport', '报告方法', '{\"footerList\":[],\"elementsList\":[]}', 0, 0, 0, '2022-12-15 17:41:48', 0, 0);
