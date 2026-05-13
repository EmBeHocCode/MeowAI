import type { ChatResponse, DashboardSummary, IntentsResponse, ProductsResponse } from './types';

async function requestJson<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...(init?.headers ?? {}),
    },
  });

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export function getDashboardSummary() {
  return requestJson<DashboardSummary>('/api/meowai/api/dashboard/summary');
}

export function getProducts() {
  return requestJson<ProductsResponse>('/api/meowai/api/products');
}

export function getIntents() {
  return requestJson<IntentsResponse>('/api/meowai/api/intents');
}

export function sendChatMessage(message: string) {
  return requestJson<ChatResponse>('/api/meowai/chat', {
    method: 'POST',
    body: JSON.stringify({ message }),
  });
}
