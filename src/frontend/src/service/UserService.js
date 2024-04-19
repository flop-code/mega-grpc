import { BACKEND_URL, postQuery, getQuery } from "./config"

export const api_current_user = async () => {
    const response = await getQuery(`${BACKEND_URL}/user/current_user`);
    return response;
};

export const api_login = async (data) => {
    const response = await postQuery(`${BACKEND_URL}/user/login`, data);
    return response;
};


export const api_logout = async () => {
    const response = await postQuery(`${BACKEND_URL}/user/logout`);
    return response;
};
