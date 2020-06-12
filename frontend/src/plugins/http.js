import Vue from "vue";
import axios from "axios";
import VuetifyToast from "vuetify-toast-snackbar";

axios.interceptors.response.use(
  response => {
    if (response.status === 202) {
      Vue.prototype.$toast.info("You request has been queued", {
        icon: "mdi-information",
        color: "green"
      });
    } else if (response.status === 201) {
      Vue.prototype.$toast.info("Operation successful", {
        icon: "mdi-check",
        color: "green"
      });
    }
    return response;
  },
  error => {
    if (error.response.status === 400) {
      Vue.prototype.$toast.error("Bad or malformed request.", {
        icon: "mdi-alert-circle",
        color: "red"
      });
    } else if (error.response.status === 409) {
      Vue.prototype.$toast.error("Cannot add duplicates in the system.", {
        icon: "mdi-alert-circle",
        color: "red"
      });
    } else if (error.response.status > 409 && error.response.status < 502) {
      Vue.prototype.$toast.error("Operation failed", {
        icon: "mdi-alert-circle",
        color: "red"
      });
    } else if (error.response.status === 502) {
      Vue.prototype.$toast.info("Server is down", {
        icon: "mdi-check",
        color: "green"
      });
    }
    return Promise.reject(error.response);
  }
);

Vue.prototype.$http = axios;
Vue.use(VuetifyToast, {
  x: "center",
  y: "top",
  dismissable: true,
  property: "$toast"
});
