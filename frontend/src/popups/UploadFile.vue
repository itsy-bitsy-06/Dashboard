<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" width="70%">
      <template v-slot:activator="{ on }">
        <v-btn color="purple darken-1" icon v-on="on">
          <v-icon>mdi-attachment</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title class="headline">Select File tp upload</v-card-title>
        <v-col cols="10" offset="1">
          <v-file-input
            accept="application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            v-model="file"
            hide-input
            show-size
            label="File input"
          ></v-file-input>
        </v-col>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="validate_and_save"
            :disabled="file === null"
          >
            Upload
          </v-btn>
          <v-btn color="error darken-3" text @click="dialog = false">
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  data: () => ({
    dialog: false,
    file: null
  }),
  methods: {
    async validate_and_save() {
      const formData = new FormData();
      formData.append("file", this.file);
      await this.$http.post(`${this.baseUrl}/api/dashboard`, formData);
      this.file = null;
      this.dialog = false;
    }
  }
};
</script>
