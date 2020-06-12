<template>
  <v-navigation-drawer
    app
    expand-on-hover
    :mini-variant="true"
    :permanent="true"
    dark
    class="black"
  >
    <v-list dense nav>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            <v-icon color="lime accent-1" class="mr-4 ml-0 pr-4 pl-0"
              >mdi-lightbulb</v-icon
            >
            {{ VUE_APP_VERSION }}
          </v-list-item-title>
          <v-list-item-subtitle></v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list-item v-for="item in items" :key="item.title" link :to="item.to">
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
export default {
  data() {
    return {
      items: [
        {
          title: "Dashboard",
          icon: "mdi-view-dashboard",
          to: { name: "Dashboard" }
        },
        {
          title: "Help",
          icon: "mdi-help",
          to: { name: "Help" }
        }
      ],
      right: null
    };
  }
};
</script>
<style scoped>
.v-navigation-drawer--fixed {
  z-index: 10 !important;
}
</style>
