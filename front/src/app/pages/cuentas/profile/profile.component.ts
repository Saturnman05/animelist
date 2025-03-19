import { Component, inject, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { Router } from '@angular/router';

import { NavBarComponent } from '../../../components/nav-bar/nav-bar.component';
import { AuthService } from '../../../services/auth/auth.service';
import { UserService } from '../../../services/user/user.service';
import { User } from '../../../models/user.model';

@Component({
  selector: 'app-profile',
  imports: [
    MatButtonModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatProgressSpinnerModule,
    NavBarComponent,
    ReactiveFormsModule,
  ],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.scss',
})
export class ProfileComponent implements OnInit {
  profileForm!: FormGroup;
  isEditing: boolean = false;
  isLoading: boolean = false;
  private fieldsDisabled: boolean = true;
  private userData: User = {
    user_id: '',
    username: '',
    email: '',
    password: '',
    date_registered: new Date(),
  };

  private AuthService = inject(AuthService);
  private fb = inject(FormBuilder);
  private router = inject(Router);
  private userService = inject(UserService);

  private initForm(): void {
    this.profileForm = this.fb.group({
      username: [
        {
          value: this.userData?.username || '...loading',
          disabled: this.fieldsDisabled,
        },
        Validators.required,
      ],
      email: [
        {
          value: this.userData?.email || '...loading',
          disabled: this.fieldsDisabled,
        },
        Validators.required,
      ],
    });

    this.loadUserData();
  }

  private loadUserData(): void {
    this.userService.getMyUser().subscribe({
      next: (user) => {
        this.userData = user;

        this.profileForm.controls['username'].setValue(
          this.userData?.username || 'ERROR'
        );
        this.profileForm.controls['email'].setValue(
          this.userData?.email || 'ERROR'
        );
      },
      error: (err) => {
        console.error('Error obteniendo mi usuario', err);
      },
    });
  }

  ngOnInit(): void {
    if (!this.AuthService.isAuthenticated$) {
      this.router.navigate(['/login']);
      return;
    }

    this.initForm();
  }

  onChangeEnabled(): void {
    this.isEditing = true;
    this.fieldsDisabled = true;

    this.profileForm.controls['username'].enable();
    this.profileForm.controls['email'].enable();
  }

  onChangeDisabled(): void {
    this.isEditing = false;
    this.fieldsDisabled = false;

    this.profileForm.controls['username'].disable();
    this.profileForm.controls['email'].disable();
  }

  onSubmit(): void {
    if (this.profileForm.invalid) {
      console.log('invalid form');
      return;
    }

    this.isLoading = true;

    this.userData.username = this.profileForm.controls['username'].value;
    this.userData.email = this.profileForm.controls['email'].value;

    this.userService.updateUser(this.userData).subscribe({
      next: () => {
        this.loadUserData();
        this.isLoading = false;
        this.isEditing = false;
      },
      error: (err) => {
        console.error(err);
        this.isLoading = false;
        this.isEditing = false;
      },
    });

    this.onChangeDisabled();
  }
}
