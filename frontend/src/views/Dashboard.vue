<template>
  <div>
    <Header title="Home" :crumbs="crumbs" />
    <v-container class="mt-0 pt-0">
      <v-row>
        <v-col cols="1" offset="11">
          <UploadFile @input="fetchDashboardData" />
        </v-col>
        <v-col cols="12">
          <TestChart v-if="false" />
        </v-col>
        <v-col cols="12">
          <PieChart
            title="By Status"
            field="Status"
            :data="pieStatusData"
            :key="key"
          />
        </v-col>
        <v-col cols="12">
          <PieChart
            title="By Issue Type"
            field="IssueType"
            :data="pieIssueTypeData"
            :key="key"
          />
        </v-col>
        <v-col cols="12">
          <PieChart
            title="By Resolution"
            field="Resolution"
            :data="pieResolutionData"
            :key="key"
          />
        </v-col>
        <v-col cols="12">
          <PieChart
            field="CustomerRequestType"
            title="By Customer Request Type"
            :data="pieCustomerRequestTypeData"
            :key="key"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "../components/Header";
import TestChart from "../components/TestChart";
import PieChart from "../components/PieChart";
import UploadFile from "../popups/UploadFile";

export default {
  name: "Home",
  components: {
    Header,
    TestChart,
    PieChart,
    UploadFile
  },
  data() {
    return {
      dashboard: [],
      key: 0,
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
    this.fetchDashboardData();
  },
  computed: {
    pieStatusData() {
      let statuses = ["In Progress", "Resolved"];
      return this.pieGroupDataBy(statuses, "Status");
    },
    pieIssueTypeData() {
      let issues = ["Service Request", "Bug", "Task"];
      return this.pieGroupDataBy(issues, "IssueType");
    },
    pieResolutionData() {
      let resolutions = ["Valid", "Invalid"];
      return this.pieGroupDataBy(resolutions, "Resolution");
    },
    pieCustomerRequestTypeData() {
      let crts = [
        "3D Tool",
        "Supply Chain",
        "Canvas",
        "Catalog",
        "EC Management",
        "3D-Rendering",
        "Reports"
      ];
      return this.pieGroupDataBy(crts, "CustomerRequestType");
    }
  },
  methods: {
    pieGroupDataBy(values, field) {
      let result = [];
      values.forEach(el => {
        let arr = this.dashboard.filter(f => f[field] === el);
        result.push({ Status: el, Count: arr.length });
      });
      return result;
    },
    async fetchDashboardData() {
      let dashboard = await this.$http.get(`${this.baseUrl}/api/dashboard`);
      this.dashboard = dashboard.data;
      this.key++;
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  text-decoration: none;
}
</style>
