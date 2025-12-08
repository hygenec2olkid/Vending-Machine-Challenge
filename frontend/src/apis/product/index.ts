import type {
  BuyProductRequest,
  Product,
} from "../../features/mainpage/type/api";
import Request from "../../shared/utils/request";

export const getProductList: () => Promise<Product[]> = () => {
  return Request.get("/products/stock");
};

export const buyItem: (
  payload: BuyProductRequest
) => Promise<Record<number, number>> = (payload) => {
  return Request.post("/products/purchase", payload);
};
