export const BACKEND_URL = "http://localhost:8080/api" //`${window.location.origin}/api`

const request = async (url, options) => {
    try {
        const response = await fetch(url, options);
        const resData = await response.json();
        return {
            status: response.status,
            success: response.ok,
            message: resData && resData.detail
                ? JSON.stringify(resData.detail)
                : response.ok
                    ? "Success."
                    : `Error! ${response.statusText}`,
            data: resData,
        };
    } catch (error) {
        return {
            status: 400,
            success: false,
            message: "Something went wrong. " + error.message,
            data: { detail: error.message },
        };
    }
};

export const postQuery = async (url, data) => {
    const requestOptions = {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    };

    return request(url, requestOptions);
};

export const getQuery = async (url) => {
    const requestOptions = {
        method: "GET",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
        },
    };

    return request(url, requestOptions);
};


export const deleteQuery = async (url) => {
    const requestOptions = {
        method: "DELETE",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
        },
    }

    return request(url, requestOptions);
}