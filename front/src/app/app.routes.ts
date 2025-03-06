import { Routes } from '@angular/router';
import { LoginComponent } from './pages/cuentas/login/login.component';
import { ProfileComponent } from './pages/cuentas/profile/profile.component';

export const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'profile', component: ProfileComponent },
  { path: '**', redirectTo: '', pathMatch: 'full' },
];
