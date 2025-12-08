import axios from "axios";

const axiosClient = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  timeout: 1200000,
});

const get = async <T = unknown>(path: string): Promise<T> => {
  const res = await axiosClient.get<T>(path);
  return res.data;
};

const post = async <T = unknown, D = unknown>(
  path: string,
  data: D
): Promise<T> => {
  const res = await axiosClient.post<T>(path, data);
  return res.data;
};

const put = async <T = unknown, D = unknown>(
  path: string,
  data: D
): Promise<T> => {
  const res = await axiosClient.put<T>(path, data);
  return res.data;
};

const deleted = async <T = unknown>(path: string): Promise<T> => {
  const res = await axiosClient.delete<T>(path);
  return res.data;
};

const Request = {
  get,
  post,
  put,
  deleted,
};

export default Request;
