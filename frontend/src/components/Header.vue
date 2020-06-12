<template>
  <v-banner single-line :sticky="true">
    <template v-slot:default>
      <v-breadcrumbs class="ml-4 pl-4" :items="crumbs" large></v-breadcrumbs>
    </template>
    <template v-slot:actions>
      <v-col cols="6" v-if="isSearchVisible">
        <v-text-field
          label="Filter"
          @click:append="
            inverted = !inverted;
            updateSearch();
          "
          :append-icon="inverted ? 'mdi-eye-off' : 'mdi-eye'"
          :value="searchInput"
          v-model="query"
          @input="updateSearch"
        ></v-text-field>
      </v-col>
    </template>
  </v-banner>
</template>
<script>
import { mapState } from "vuex";

export default {
  props: {
    title: {
      type: String,
      default: "Home"
    },
    crumbs: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      query: "",
      inverted: false
    };
  },
  computed: {
    ...mapState(["searchInput", "isSearchVisible"])
  },
  methods: {
    updateSearch() {
      this.$store.commit("SEARCH", {
        value: this.query,
        inverted: this.inverted,
        visible: this.isSearchVisible
      });
    }
  }
};
</script>
<style scoped>
.v-banner--single-line {
  z-index: 9 !important;
}
</style>
