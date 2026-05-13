import type { DashboardSummary } from '@/lib/types';

export function StatusPanel({ summary }: { summary: DashboardSummary }) {
  return (
    <article className="panel">
      <div className="panel-heading">
        <div>
          <h2>Thông tin bot</h2>
          <p>Giai đoạn và engine đang dùng.</p>
        </div>
      </div>
      <dl className="info-list">
        <div>
          <dt>Phase</dt>
          <dd>{summary.phase}</dd>
        </div>
        <div>
          <dt>Chế độ</dt>
          <dd>{summary.mode}</dd>
        </div>
        <div>
          <dt>Tổng tồn kho mẫu</dt>
          <dd>{summary.total_stock}</dd>
        </div>
      </dl>
    </article>
  );
}
