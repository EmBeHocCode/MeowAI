type MetricCardProps = {
  label: string;
  value: string | number;
  tone?: 'pink' | 'green' | 'blue' | 'orange';
};

export function MetricCard({ label, value, tone = 'pink' }: MetricCardProps) {
  return (
    <article className={`metric-card metric-card-${tone}`}>
      <span>{label}</span>
      <strong>{value}</strong>
    </article>
  );
}
