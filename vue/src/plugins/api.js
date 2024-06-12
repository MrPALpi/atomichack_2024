import axios from "axios";
import * as toast from './toast'



const axiosInstance = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
    headers: {
        "Content-type": "application/json",
    },
});

axiosInstance.interceptors.request.use(
    function (config) {
        // Do something before request is sent
        return config;
    },
    function (error) {
        // Do something with request error
        toast.error('Error', 'Something went wrong');
        console.error(error);
        return Promise.reject(error);
    }
);

axiosInstance.interceptors.response.use(
    function (response) {
        // Any status code that lie within the range of 2xx cause this function to trigger
        // Do something with response data


        return response;
    },
    function (error) {
        // Any status codes that falls outside the range of 2xx cause this function to trigger
        // Do something with response error
        toast.error('Error', 'Something went wrong');
        console.error(error);
        return Promise.reject(error);
    }
);

export { axiosInstance };