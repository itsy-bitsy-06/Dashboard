<template>
  <div>
    <Header title="Help" :crumbs="crumbs" />
    <v-tabs icons-and-text grow>
      <v-tab>
        <v-icon left>mdi-information</v-icon>
        About
      </v-tab>
      <v-tab>
        <v-icon left>mdi-help</v-icon>
        FAQ
      </v-tab>
      <v-tab-item>
        <Editor mode="viewer" nativeEmoji :outline="false" v-model="about" />
      </v-tab-item>
      <v-tab-item>
        <Editor
          mode="viewer"
          nativeEmoji
          :outline="false"
          :preview="true"
          v-model="help"
        />
      </v-tab-item>
    </v-tabs>
  </div>
</template>
<script>
import { Editor } from "vuetify-markdown-editor";
import Header from "../components/Header";
import About from "../../../README.md";
import Help from "../../../documents/Help.md";

import { mapState } from "vuex";
import _ from "lodash";

export default {
  name: "help",
  components: {
    Editor,
    Header
  },
  data() {
    return {
      about: About,
      help: Help,
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
          text: "Help",
          exact: true,
          disabled: true,
          to: {
            name: "Help"
          }
        }
      ]
    };
  },
  computed: {
    ...mapState(["searchInput"])
  },
  watch: {
    searchInput: _.debounce(function(newQuery) {
      this.doSearch(newQuery, "#00FF00");
    }, 1000)
  },
  mounted() {
    this.$store.commit("SEARCH", {
      value: "",
      inverted: false,
      visible: true
    });
  },
  methods: {
    doSearch(text, backgroundColor) {
      if (window.find && window.getSelection) {
        document.designMode = "on";
        var sel = window.getSelection();
        sel.collapse(document.body, 0);
        while (window.find(text)) {
          document.execCommand("HiliteColor", false, backgroundColor);
          sel.collapseToEnd();
        }
        document.designMode = "off";
      }
    }
  }
};
</script>
<style>
div.markdown-text table tr td {
  border: 1px solid;
  padding-right: 10px;
  padding-left: 10px;
}
div.markdown-text table th {
  border: 2px solid;
  padding-right: 10px;
  padding-left: 10px;
}
</style>
