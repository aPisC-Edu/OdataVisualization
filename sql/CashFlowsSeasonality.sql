drop table #function_parameter;
drop table #seasonality_statistics;

delete from "envduv_forecast.db.data::CashFlowsSeasonality";

create local temporary table #function_parameter      like "envduv_forecast.db.hdb.pal::common.tt_parameter";
create local temporary table #seasonality_statistics  like "envduv_forecast.db.hdb.pal::common.tt_statistics";

insert into #function_parameter values ('ALPHA' , null , 0.2, null);

call "envduv_forecast.db.hdb.pal.afllang::seasonality_test" (
  "envduv_forecast.db.hdb.pal.views::CashFlows",
  #function_parameter,
  #seasonality_statistics,
  "envduv_forecast.db.data::CashFlowsSeasonality"
) with overview;