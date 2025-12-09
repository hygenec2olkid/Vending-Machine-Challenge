export type Coin = {
  coin: number;
  quantity: number;
};

export type Product = {
  id: number;
  name: string;
  price: number;
  quantity: number;
  img_url: string;
};

export type BuyProductRequest = {
  id: number;
  quality: number;
  balance: number;
};

export type AddCoinIntoStockRequest = {
  coin: number;
  quantity: number;
};
