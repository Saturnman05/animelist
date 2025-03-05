import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteAnimeComponent } from './delete-anime.component';

describe('DeleteAnimeComponent', () => {
  let component: DeleteAnimeComponent;
  let fixture: ComponentFixture<DeleteAnimeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DeleteAnimeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteAnimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
