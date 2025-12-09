import type {
  AddCoinIntoStockRequest,
  Coin,
} from "../../features/mainpage/type/api";
import Request from "../../shared/utils/request";

export const getCoinStock: () => Promise<Coin[]> = () => {
  return Request.get("/coins/stock");
};

export const addCoin: (payload: AddCoinIntoStockRequest) => Promise<Coin[]> = (
  payload
) => {
  return Request.post("/coins/add", payload);
};
