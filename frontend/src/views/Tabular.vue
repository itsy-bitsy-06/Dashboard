<template>
  <div>
    <Header title="Tabular" :crumbs="crumbs" />
    <GenericTable :headers="headers" :items="items" title="Jira List" />
  </div>
</template>
<script>
import Header from "../components/Header";
import GenericTable from "../components/GenericTable";

export default {
  name: "Tabular",
  components: {
    Header,
    GenericTable
  },
  data: () => ({
    crumbs: [
      {
        text: "Dashboard",
        exact: true,
        disabled: false,
        to: {
          name: "Dashboard"
        }
      },
      {
        text: "Tabular",
        exact: true,
        disabled: true,
        to: {
          name: "Tabular"
        }
      }
    ],
    headers: [
      { text: "Key", value: "Key" },
      { text: "Created", value: "Created" },
      { value: "CustomerRequestType", text: "Request Type" },
      { text: "Issue Type", value: "IssueType" },
      { text: "Resolution", value: "Resolution" },
      { text: "Status", value: "Status" }
    ],
    items: []
  }),
  created() {
    this.$store.commit("SEARCH", {
      value: "",
      inverted: false,
      visible: false
    });
  },
  async mounted() {
    let items = await this.$http.get(`${this.baseUrl}/api/dashboard`);
    items.data.map(
      f => (f.Created = new Date(f.Created + "Z").toLocaleString("en-US"))
    );
    this.items = items.data;
  },
  methods: {}
};
</script>
