import type { IntentLabel } from '@/lib/types';

export function IntentsPanel({ intents }: { intents: IntentLabel[] }) {
  return (
    <article className="panel">
      <div className="panel-heading">
        <div>
          <h2>Intent hiện có</h2>
          <p>Số câu mẫu theo từng nhóm ý định.</p>
        </div>
      </div>
      <div className="tag-list">
        {intents.map((intent) => (
          <span key={intent.intent} className="tag" title={`${intent.meaning} - Ví dụ: ${intent.example}`}>
            {intent.intent}: {intent.sample_count}
          </span>
        ))}
      </div>
    </article>
  );
}
