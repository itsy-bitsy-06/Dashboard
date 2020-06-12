<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" width="70%">
      <template v-slot:activator="{ on }">
        <v-btn color="primary darken-1" v-on="on">
          Create Group
        </v-btn>
      </template>
      <v-card>
        <v-card-title class="headline">Create Group</v-card-title>
        <v-col cols="10" offset="1">
          <v-form ref="form" v-model="valid" :lazy-validation="lazy">
            <v-row>
              <v-col cols="10" offset="1">
                <v-text-field
                  v-model="name"
                  :rules="nameRules"
                  label="Name"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="description"
                  label="Description"
                ></v-text-field>
                <v-select
                  v-model="os"
                  :items="oses"
                  label="Operating System"
                  required
                ></v-select>
                <v-text-field
                  v-model="username"
                  label="Username"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="password"
                  label="Password"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-form>
        </v-col>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="validate_and_save">
            Save
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
    valid: true,
    name: "",
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 255) || "Must be less than 255 characters"
    ],
    description: "",
    oses: ["Windows", "Linux", "OsX"],
    os: "Windows",
    username: "",
    password: "",
    lazy: false
  }),
  methods: {
    async validate_and_save() {
      if (this.$refs.form.validate()) {
        let group = {
          name: this.name,
          username: this.username,
          password: this.password,
          description: this.description,
          os: this.os
        };
        await this.$http.post(`${this.baseUrl}/api/groups`, group);
        this.$refs.form.reset();
        this.dialog = false;
        this.$emit("input");
      }
    }
  }
};
</script>
