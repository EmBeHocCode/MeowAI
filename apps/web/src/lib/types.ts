export type DashboardSummary = {
  service: string;
  status: string;
  phase: string;
  mode: string;
  product_count: number;
  total_stock: number;
  intent_count: number;
  training_samples: number;
};

export type Product = {
  id: string;
  name: string;
  category: string;
  price: string;
  stock: string;
  description: string;
  use_cases: string;
  url: string;
  formatted_price: string;
};

export type ProductsResponse = {
  products: Product[];
};

export type IntentLabel = {
  intent: string;
  meaning: string;
  example: string;
  sample_count: number;
};

export type IntentsResponse = {
  intents: IntentLabel[];
};

export type ChatResponse = {
  reply: string;
  intent: string;
};
