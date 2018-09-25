export const apiCall = (path, params) => {
    // Return a promise of a api get
    return axios({
        method: "get",
        url: path,
        params: params,
        timeout: 5000 // timeout after 5 seconds
    }).then(({ data }) => {
        // Unpack the data object and return its body
        return data.message;
    });
};
