import type { Coin } from "../../features/mainpage/type/api";
import Request from "../../shared/utils/request";

export const getCoinStock: () => Promise<Coin[]> = () => {
  return Request.get("/coins/stock");
};
