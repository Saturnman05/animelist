import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditAnimeComponent } from './edit-anime.component';

describe('EditAnimeComponent', () => {
  let component: EditAnimeComponent;
  let fixture: ComponentFixture<EditAnimeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditAnimeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditAnimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
