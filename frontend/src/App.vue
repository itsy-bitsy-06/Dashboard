<template>
  <v-app>
    <Drawer />
    <v-content>
      <router-view></router-view>
      <v-snackbar
        bottom
        right
        style="text-transform: capitalize !important;"
        v-if="event"
        :color="colors[event.status]"
        v-model="snackbar"
        :timeout="5000"
      >
        {{ event.text }}
      </v-snackbar>
    </v-content>
  </v-app>
</template>

<script>
import Drawer from "./components/Drawer";
import _ from "lodash";

export default {
  name: "App",
  components: {
    Drawer
  },
  data() {
    return {
      snackbar: false,
      event: null
    };
  },
  sockets: {
    async disconnect() {
      // console.log(`WS Disconnected ${this.$socket.connected}`);
      while (!this.$socket.connected) {
        await new Promise(resolve => setTimeout(resolve, 10000));
        await this.$socket.connect();
      }
    },
    connect_error() {
      /* eslint-disable no-console */
      console.clear();
      /* eslint-enable no-console */
    },
    connect_timeout() {
      /* eslint-disable no-console */
      console.clear();
      /* eslint-enable no-console */
    },
    UPDATED: _.debounce(function(val) {
      val = JSON.parse(val);
      let text = `${val.table} updated with status ${val.status}`.toLowerCase();
      if (val.status === "NA")
        text = `${val.table} progress updated`.toLowerCase();
      if (["Tasks", "Journals"].indexOf(val.table) > -1) {
        this.event = { text: text, status: val.status };
        this.snackbar = true;
      }
    }, 1000)
  }
};
</script>
<style>
::-webkit-scrollbar {
  width: 3px;
  height: 3px;
}
::-webkit-scrollbar-track {
  background: white;
}
::-webkit-scrollbar-thumb {
  background: #ddd;
  visibility: hidden;
}
::-webkit-scrollbar-thumb {
  visibility: visible;
}
.v-breadcrumbs__item--disabled {
  font-weight: 1000 !important;
  font-size: 2em;
}
.themed-list {
  background-color: black !important;
}
.v-data-table-header {
  background-color: black !important;
}
</style>
