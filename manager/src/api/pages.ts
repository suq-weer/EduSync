// src/api/pages.ts
export class PageController {
  private current_page: number;
  private max_page_count: number;
  private button_1: string = "none";
  private button_1_text: string = "";
  private button_2: string = "none";
  private button_2_text: string = "";
  private button_3: string = "none";
  private button_3_text: string = "";
  private button_4: string = "none";
  private button_4_text: string = "";
  private button_5: string = "none";
  private button_5_text: string = "";

  constructor(current_page: number, max_page_count: number) {
    if (current_page < 1 || max_page_count < 0) {
      throw new Error('current_page must be >= 1 and max_page_count must be >= 0');
    }

    this.current_page = current_page;
    this.max_page_count = max_page_count;

    this.setButtons();
  }

  private setButtons() {
    this.button_1 = "none";
    this.button_2 = "none";
    this.button_3 = "none";
    this.button_4 = "none";
    this.button_5 = "none";

    if (this.max_page_count === 0 || this.max_page_count === 1) {
      this.button_1 = "visible";
      this.button_1_text = "1";
    } else if (this.max_page_count === 2) {
      this.button_1 = "visible";
      this.button_1_text = "1";
      this.button_2 = "visible";
      this.button_2_text = "2";
    } else if (this.max_page_count === 3) {
      this.button_1 = "visible";
      this.button_1_text = "1";
      this.button_2 = "visible";
      this.button_2_text = "2";
      this.button_3 = "visible";
      this.button_3_text = "3";
    } else if (this.max_page_count === 4) {
      this.button_1 = "visible";
      this.button_1_text = "1";
      this.button_2 = "visible";
      this.button_2_text = "2";
      this.button_3 = "visible";
      this.button_3_text = "3";
      this.button_5 = "visible";
      this.button_5_text = "4";
    } else if (this.max_page_count === 5) {
      this.button_1 = "visible";
      this.button_1_text = "1";
      this.button_2 = "visible";
      this.button_2_text = "2";
      this.button_3 = "visible";
      this.button_3_text = "3";
      this.button_4 = "visible";
      this.button_4_text = "4";
      this.button_5 = "visible";
      this.button_5_text = "5";
    } else if (this.max_page_count > 5) {
      const minPage = Math.max(1, this.current_page - 2);
      const maxPage = Math.min(this.max_page_count, this.current_page + 2);

      this.button_1 = "visible";
      this.button_1_text = minPage.toString();
      this.button_2 = "visible";
      this.button_2_text = (minPage + 1).toString();
      this.button_3 = "visible";
      this.button_3_text = "......";
      this.button_4 = "visible";
      this.button_4_text = (maxPage - 1).toString();
      this.button_5 = "visible";
      this.button_5_text = maxPage.toString();
    }
  }

  nextPage() {
    if (this.current_page < this.max_page_count && this.max_page_count > 0) {
      this.current_page++;
      this.setButtons();
    }
    return { "current_page": this.current_page };
  }

  backPage() {
    if (this.current_page > 1) {
      this.current_page--;
      this.setButtons();
    }
    return { "current_page": this.current_page };
  }

  private getResult() {
    return {
      "current_page": this.current_page,
      "max_page_count": this.max_page_count,
      "button_1": this.button_1,
      "button_1_text": this.button_1_text,
      "button_2": this.button_2,
      "button_2_text": this.button_2_text,
      "button_3": this.button_3,
      "button_3_text": this.button_3_text,
      "button_4": this.button_4,
      "button_4_text": this.button_4_text,
      "button_5": this.button_5,
      "button_5_text": this.button_5_text,
    };
  }
}
