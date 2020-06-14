<template>
  <div>
    <H1 class="mb-1 text-left secondary--text">{{ title }}</H1>
    <div class="test" ref="chartdiv"></div>
  </div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import am4themes_dark from "@amcharts/amcharts4/themes/dark";
import am4themes_material from "@amcharts/amcharts4/themes/material";

am4core.useTheme(am4themes_animated);
am4core.useTheme(am4themes_dark);
am4core.useTheme(am4themes_material);

export default {
  name: "PieChart",
  props: {
    data: {
      type: Array,
      default: () => []
    },
    value: {
      type: String,
      default: "Count"
    },
    status: {
      type: String,
      default: "Status"
    },
    title: {
      type: String,
      default: "What"
    }
  },
  mounted() {
    let chart = am4core.create(this.$refs.chartdiv, am4charts.PieChart3D);
    chart.data = this.data;
    chart.innerRadius = am4core.percent(40);
    chart.depth = 120;
    chart.legend = new am4charts.Legend();
    var series = chart.series.push(new am4charts.PieSeries3D());
    series.dataFields.value = this.value;
    series.dataFields.depthValue = this.value;
    series.dataFields.category = this.status;
    series.slices.template.cornerRadius = 5;
    series.colors.step = 3;
    this.chart = chart;
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.dispose();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.test {
  width: 100%;
  height: 500px;
}
</style>
