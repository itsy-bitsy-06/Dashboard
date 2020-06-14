<template>
  <v-card>
    <v-card-title>
      {{ title }}
      <v-spacer />
      <v-btn
        :disabled="!items.length"
        text
        icon
        class="pink darken-2"
        @click="DownloadExcel"
      >
        <v-icon color="blue-grey darken-2">
          mdi-download
        </v-icon>
      </v-btn>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="filteredItems"
      hide-default-header
      hide-default-footer
      pa-4
      max-width="1024px"
      height="700"
      fixed-header
      disable-pagination
    >
      <!-- HEADERS -->
      <template v-slot:header="{ props: { headers } }">
        <thead>
          <tr>
            <th v-for="header in headers" :key="header.text" class="filter-row">
              <p class="font-weight-bold text-center white--text">
                {{ header.text }}
              </p>
              <v-text-field
                solo
                v-model="query[header.value]"
                type="text"
                placeholder=""
              >
              </v-text-field>
            </th>
          </tr>
        </thead>
      </template>

      <!-- TABLE BODY -->
      <template v-slot:item="{ item }">
        <tr class="text-center" justify="center" align="center">
          <td max-width="10%" v-for="i in headers" :key="i.value">
            {{ item[i.value] }}
          </td>
        </tr>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import Excel from "../utils/Excel";

export default {
  name: "GenericTable",
  props: {
    headers: {
      type: Array,
      default: () => []
    },
    items: {
      type: Array,
      default: () => []
    },
    title: {
      type: String,
      default: "Unknown"
    }
  },
  data() {
    return {
      query: {}
    };
  },
  mounted() {
    this.query = this.$route.query;
  },
  computed: {
    filteredItems: function() {
      let res = this.items;
      let headers = this.headers;
      let query = this.query || {};
      for (let i = 0; i < headers.length; i++) {
        let val = headers[i].value;
        res = res.filter(row => !query[val] || row[val].startsWith(query[val]));
      }
      return res;
    }
  },
  methods: {
    async DownloadExcel() {
      let data = this.filteredItems;
      let today = new Date();
      let filename = `${this.title}_${today.toLocaleString()}.xlsx`;
      let excel = new Excel();
      excel.AddWorkSheetToBook(data, this.title);
      excel.SaveAs(filename);
    }
  }
};
</script>
<style scoped>
.filter {
  border-bottom: 1px solid;
  border-top: 1px solid;
  border-left: 1px solid;
  border-right: 1px solid;
  border-radius: 5px;
  background-color: white;
  margin-bottom: 10px;
  margin-top: -10px;
}
.filter-row {
  background-color: #b3b6b7 !important;
}
</style>
