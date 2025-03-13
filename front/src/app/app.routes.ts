import { Routes } from '@angular/router';
import { LoginComponent } from './pages/cuentas/login/login.component';
import { ProfileComponent } from './pages/cuentas/profile/profile.component';
import { ListAnimesComponent } from './pages/animes/list-animes/list-animes.component';

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'register', component: ProfileComponent },
  { path: 'animes', component: ListAnimesComponent },
  { path: '**', redirectTo: '', pathMatch: 'full' },
];
