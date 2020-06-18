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
