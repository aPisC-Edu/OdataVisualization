drop table #function_header;
drop table #operation_config;
drop table #variable_descs;
drop table #variable_roles;

drop table #operation_log;
drop table #summary;
drop table #indicators;

delete from "envduv_forecast.db.data::CashFlowsForecast";

create local temporary table #function_header  like "envduv_forecast.db.hdb.apl::forecast.tt_function_header";
create local temporary table #operation_config like "envduv_forecast.db.hdb.apl::forecast.tt_operation_config";
create local temporary table #variable_descs   like "envduv_forecast.db.hdb.apl::forecast.tt_variable_descs";
create local temporary table #variable_roles   like "envduv_forecast.db.hdb.apl::forecast.tt_variable_roles";

create local temporary table #operation_log    like "envduv_forecast.db.hdb.apl::forecast.tt_operation_log";
create local temporary table #summary          like "envduv_forecast.db.hdb.apl::forecast.tt_summary";
create local temporary table #indicators       like "envduv_forecast.db.hdb.apl::forecast.tt_indicators";

insert into #function_header values ('Oid', '#42');
insert into #function_header values ('LogLevel', '8');

insert into #operation_config values ('APL/TimePointColumnName'   , 'signal_time'              , null);
insert into #operation_config values ('APL/ApplyExtraMode'        , 'Forecasts and Error Bars' , null);
insert into #operation_config values ('APL/LastTrainingTimePoint' , '2001-12-28', null);
insert into #operation_config values ('APL/Horizon'               , '21'        , null);

insert into #variable_descs values (0, 'signal_time'  , 'date'     , 'continuous', 1, 1, null, null, null, null);
insert into #variable_descs values (1, 'signal_value' , 'number'   , 'continuous', 0, 0, null, null, null, null);

insert into  #variable_roles values ('signal_time'  , 'input' , NULL, NULL, '#1');
insert into  #variable_roles values ('signal_value' , 'target', NULL, NULL, '#1');

call "envduv_forecast.db.hdb.apl.afllang::forecast" (
  #function_header,
  #operation_config,
  #variable_descs,
  #variable_roles,
  "envduv_forecast.db.data::CashFlows",
  "envduv_forecast.db.data::CashFlowsForecast",
  #operation_log,
  #summary,
  #indicators
) with overview;