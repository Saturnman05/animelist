import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterAnimeComponent } from './register-anime.component';

describe('RegisterAnimeComponent', () => {
  let component: RegisterAnimeComponent;
  let fixture: ComponentFixture<RegisterAnimeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RegisterAnimeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegisterAnimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
