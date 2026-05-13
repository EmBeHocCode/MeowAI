import Link from 'next/link';
import { IntentsPanel } from '@/components/dashboard/intents-panel';
import { MetricCard } from '@/components/dashboard/metric-card';
import { ProductsTable } from '@/components/dashboard/products-table';
import { StatusPanel } from '@/components/dashboard/status-panel';
import type { DashboardSummary, IntentsResponse, ProductsResponse } from '@/lib/types';
import './dashboard.css';

export const dynamic = 'force-dynamic';

async function getServerJson<T>(path: string): Promise<T> {
  const baseUrl = process.env.MEOWAI_API_BASE ?? 'http://127.0.0.1:8020';
  const response = await fetch(`${baseUrl}${path}`, { cache: 'no-store' });

  if (!response.ok) {
    throw new Error(`Cannot load ${path}`);
  }

  return response.json() as Promise<T>;
}

export default async function DashboardPage() {
  const [summary, products, intents] = await Promise.all([
    getServerJson<DashboardSummary>('/api/dashboard/summary'),
    getServerJson<ProductsResponse>('/api/products'),
    getServerJson<IntentsResponse>('/api/intents'),
  ]);

  return (
    <div className="dashboard-page">
      <header className="page-header">
        <div>
          <p className="eyebrow">Bot workspace</p>
          <h1>Dashboard quản lý MeowAI</h1>
          <p className="muted">Theo dõi trạng thái bot, dữ liệu sản phẩm và dataset intent.</p>
        </div>
        <Link className="primary-link" href="/chat">
          Mở chat thử
        </Link>
      </header>

      <section className="metric-grid" aria-label="Chỉ số bot">
        <MetricCard label="Trạng thái" value={summary.status} tone="green" />
        <MetricCard label="Sản phẩm" value={summary.product_count} tone="blue" />
        <MetricCard label="Câu dataset" value={summary.training_samples} tone="pink" />
        <MetricCard label="Intent" value={summary.intent_count} tone="orange" />
      </section>

      <section className="dashboard-grid">
        <StatusPanel summary={summary} />
        <IntentsPanel intents={intents.intents} />
      </section>

      <ProductsTable products={products.products} />
    </div>
  );
}
