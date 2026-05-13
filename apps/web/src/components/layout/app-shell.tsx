import { SidebarNav } from './sidebar-nav';

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="app-frame">
      <SidebarNav />
      <main className="main-content">{children}</main>
    </div>
  );
}
