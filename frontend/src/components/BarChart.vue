<template>
  <v-card class="mx-auto" :color="color" width="100%">
    <v-card-title>
      <v-row align="center" no-gutters>
        <div class="caption text-uppercase text-right mr-4">
          {{ title }}
        </div>
        <div>
          <span class="display-2 font-weight-black" v-text="total"></span>
        </div>
      </v-row>
    </v-card-title>

    <v-sheet color="transparent">
      <v-sparkline
        :gradient="gradient"
        :line-width="6"
        :type="bartype"
        :labels="labels"
        :show-labels="true"
        :value="heartbeats"
      ></v-sparkline>
    </v-sheet>
  </v-card>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: ""
    },
    color: {
      type: String,
      default: "black"
    },
    data: {
      type: Object
    },
    field: {
      type: String,
      default: ""
    },
    gradient: {
      type: Array,
      default: () => ["purple", "violet"]
    }
  },
  computed: {
    heartbeats() {
      return Object.values(this.data[this.field]);
    },
    labels() {
      return Object.keys(this.data[this.field]);
    },
    bartype() {
      let nonzero = this.heartbeats.find(e => e > 0);
      return nonzero ? "bar" : "trend";
    },
    total() {
      const sum = this.heartbeats.reduce((acc, cur) => acc + cur, 0);
      return sum;
    }
  }
};
</script>
