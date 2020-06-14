<template>
  <div>
    <Header title="Home" :crumbs="crumbs" />
    <v-row class="mx-4" no-gutter>
      <v-col cols="1" offset="11">
        <UploadFile />
      </v-col>
      <v-col cols="3">
        <InfoChart
          title="Server Process Mem "
          color="blue-grey lighten-4"
          units=" %"
          :data="healthData"
          field="mempc"
        />
      </v-col>
      <v-col cols="3">
        <InfoChart
          title="CPU "
          color="blue-grey lighten-3"
          units=" %"
          :data="healthData"
          field="cpu"
        />
      </v-col>
      <v-col cols="3">
        <InfoChart
          title="Network connections "
          color="blue-grey lighten-2"
          units=""
          :data="healthData"
          field="net"
        />
      </v-col>
      <v-col cols="3">
        <InfoChart
          title="Memory Available "
          color="blue-grey lighten-1"
          units=" %"
          :data="healthData"
          field="memtotal"
        />
      </v-col>
    </v-row>
    <v-container class="mt-0 pt-0">
      <!-- <v-row dense v-if="dashboard">
        <v-col cols="6">
          <BarChart
            title="Tests Passed this Week"
            color="blue-grey darken-1"
            :gradient="['success', 'green']"
            :data="dashboard"
            field="week_pass"
          />
        </v-col>
        <v-col cols="6">
          <BarChart
            title="Tests Failed this Week"
            color="blue-grey darken-2"
            :gradient="['error', 'red']"
            :data="dashboard"
            field="week_fail"
          />
        </v-col>
      </v-row> -->
      <TestChart />
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue from "vue";
import Header from "../components/Header";
import InfoChart from "../components/InfoChart";
// import BarChart from "../components/BarChart";
import TestChart from "../components/TestChart";
import UploadFile from "../popups/UploadFile";

export default {
  name: "Home",
  components: {
    Header,
    InfoChart,
    // BarChart,
    TestChart,
    UploadFile
  },
  data() {
    return {
      dashboard: null,
      crumbs: [
        {
          text: "Dashboard",
          exact: true,
          disabled: true,
          to: {
            name: "Dashboard"
          }
        }
      ]
    };
  },
  async created() {
    this.$store.commit("SEARCH", {
      value: "",
      inverted: false,
      visible: false
    });
    let dashboard = await this.$http.get(`${this.baseUrl}/api/dashboard`);
    this.dashboard = dashboard.data;
    for (let i = 0; i < 20; i++) {
      this.healthData.unshift({ cpu: 0, mempc: 0, net: 0, memtotal: 0 });
    }
    Vue.nextTick(this.pollHealth);
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  text-decoration: none;
}
</style>
